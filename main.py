import os
import csv
import argparse

import vocab_from_links
import kanji_from_links
import kanji_link_from_search
import verb_inflections_from_search


def get_links_from_file(input_path, output_path):
    url_list = []
    if not os.path.isfile(input_path) and not os.path.isfile(output_path):
        print('Input and/or output file do not exist.')
        exit()

    with open(input_path, 'r') as f:
        for line in f:
            if link := line.strip():
                url_list.append(link)

    return url_list


def scrap_vocab(url):
    return vocab_from_links.scrap_page(url)


def scrap_kanji(url):
    return kanji_from_links.scrap_page(url)


def scrap_from_jisho(args, scrap_func):
    url_list = get_links_from_file(args.I, args.O)

    html_lists = []
    for url in url_list:
        print(f'Scraping page {url}')
        html_lists.append(scrap_func(url))

    write_to_csv(args, html_lists)


def write_to_csv(args, lists):
    with open(args.O, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in lists:
            writer.writerow(row)


def main(args):
    if card_type := args.to_card:
        scrap_func = scrap_vocab if card_type == 'vocab' else scrap_kanji
        scrap_from_jisho(args, scrap_func)
    elif args.list == 'kanji':
        kanji_link_from_search.list_kanji_from_search(args.search_url, args.O)
    elif args.verb_inflections:
        verb_inflections_from_search.search_all(args)
    else:
        print(f"Nothing to do. Check arguments.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Anki cards from Jisho links.')
    parser.add_argument('-I', type=str, help='Input file path for Jisho links')
    parser.add_argument('-O', type=str, help='Output file path for Anki cards')
    parser.add_argument('-u', '--search_url', type=str, help='Search URL for listing all links')
    parser.add_argument('--verb_search_tags', type=str, nargs='+', default=['n1'], help='Search tags for verbs')
    parser.add_argument('--verb_pos', type=str, nargs='+',
                        default=['v5b', 'v5g', 'v5k', 'v5m', 'v5n', 'v5r', 'v5s', 'v5t', 'v5u', 'v1'],
                        help='Verbs ending with')

    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('--to_card', nargs='?', choices=['vocab', 'kanji'],
                              help='Turn list of vocab/kanji Jisho links to Anki cards.')
    action_group.add_argument('--list', nargs='?', choices=['kanji'],
                              help='Do a Jisho search and get all links, write them down to a text file.')
    action_group.add_argument('--verb_inflections', action='store_true',
                              help='Do a Jisho search and get all verb inflections, turn them into Anki cards.')
    main(parser.parse_args())
