import os
import csv
import argparse

import vocab_from_links
import kanji_from_links


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

    with open(args.O, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in html_lists:
            writer.writerow(row)


def main(args):
    if card_type := args.to_card:
        # if card_type == 'vocab' and 'ANKI_MEDIA_PATH' not in os.environ:
        #     print('ANKI_MEDIA_PATH is not in environment variables. Please specify Anki collection.media path.')
        #     print(os.environ)
        #     exit()
        # else:
        #     ANKI_MEDIA_PATH = os.environ['ANKI_MEDIA_PATH']
        #     print('Audio files will be saved to Anki media path: ', ANKI_MEDIA_PATH)
        scrap_func = scrap_vocab if card_type == 'vocab' else scrap_kanji
        scrap_from_jisho(args, scrap_func)
    else:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Anki cards from Jisho links.')
    parser.add_argument('-I', type=str, help='Input file path for Jisho links')
    parser.add_argument('-O', type=str, help='Output file path for Anki cards')
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('--to_card', default='vocab', nargs='?', choices=['vocab', 'kanji'],
                              help='Turn list of vocab/kanji Jisho links to Anki cards.')
    action_group.add_argument('--list', default='kanji', nargs='?', choices=['kanji'],
                              help='Do a Jisho search and get all links, write them down to a text file.')
    main(parser.parse_args())
