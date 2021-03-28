import requests
import os
import re
import csv
import argparse
from bs4 import BeautifulSoup

ANKI_MEDIA_PATH = ""
URL_LIST = []


def save_audio_as_mp3(source, word):
    audio_link = 'https:' + source
    audio = requests.get(audio_link)

    audio_filename = 'audio_' + word + '.mp3'
    filename = ANKI_MEDIA_PATH + '\\' + audio_filename
    with open(filename, 'wb') as audio_file:
        audio_file.write(audio.content)
    print(source)


def parse_word_info(word_soup, word):
    info_div = word_soup.find('div', attrs={'class': 'concept_light-status'})
    new_info_div = BeautifulSoup('<div class="concept_light-status"></div>', 'html.parser')

    is_common = False
    if common_span := info_div.find('span', string='Common word'):
        is_common = True
        new_info_div.div.append(common_span)

    jlpt_level = ""
    if jlpt_tag := word_soup.find('span', string=re.compile('JLPT')):
        new_info_div.div.append(jlpt_tag)
        jlpt_level = jlpt_tag.string.replace(' ', '-')

    has_audio = False
    if audio_tag := word_soup.find('audio'):
        audio_source_tag = audio_tag.find('source', attrs={'type': 'audio/mpeg'})
        save_audio_as_mp3(audio_source_tag.attrs['src'], word)
        has_audio = True

    return [new_info_div, has_audio, is_common, jlpt_level]


def parse_word(answer_div):
    word_span = answer_div.find('span', attrs={'class': 'text'})
    furigana_span = answer_div.find('span', attrs={'class': 'furigana'})

    word = word_span.string.strip()

    return [word, furigana_span]


def parse_meanings(meanings_div):
    if wiki_tags := meanings_div.find('div', string='Wikipedia definition'):
        wiki_description = wiki_tags.nextSibling
        wiki_tags.decompose()
        wiki_description.decompose()
    return meanings_div


def parse_word_page(soup):
    word_soup = soup.find('article')

    answer_div = word_soup.find('div', attrs={'class': 'concept_light-representation'})
    word_html = parse_word(answer_div)

    meanings_div = word_soup.find('div', attrs={'class': 'meanings-wrapper'})
    meanings_html = parse_meanings(meanings_div)
    word = word_html[0]

    info_list = parse_word_info(word_soup, word)
    sound_res_anki = ""
    if info_list[1]:
        sound_res_anki = '[sound:audio_' + word + '.mp3]'

    return word_html + [sound_res_anki] + [info_list[0]] + [meanings_html]


def parse_kanji_in_word_page(soup):
    kanji_soup = soup.find('div', attrs={'class': 'kanji_light_block'})
    debug_div_list = kanji_soup.find_all('div', attrs={'class': 'debug'})
    for debug_div in debug_div_list:
        print(debug_div.prettify())
        debug_div.decompose()
    return [kanji_soup]


def scrap_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find('div', id='page_container')

    word_html_list = parse_word_page(result)
    kanji_html_list = parse_kanji_in_word_page(result)

    html_list = word_html_list + kanji_html_list

    return html_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Anki cards from Jisho links.')
    parser.add_argument('-I', type=str, help='Input file path for Jisho links')
    parser.add_argument('-O', type=str, help='Output file path for Anki cards')
    args = parser.parse_args()

    INPUT_PATH = args.I
    OUTPUT_PATH = args.O

    if not os.path.isfile(INPUT_PATH) and not os.path.isfile(OUTPUT_PATH):
        print('Input and/or output file do not exist.')
        exit()

    with open(INPUT_PATH, 'r') as f:
        for line in f:
            if link := line.strip():
                URL_LIST.append(link)
    print(URL_LIST)

    if 'ANKI_MEDIA_PATH' not in os.environ:
        print('ANKI_MEDIA_PATH is not in environment variables. Please specify Anki collection.media path.')
        print(os.environ)
        exit()
    else:
        ANKI_MEDIA_PATH = os.environ['ANKI_MEDIA_PATH']
        print('Audio files will be saved to Anki media path: ', ANKI_MEDIA_PATH)

    html_lists = []
    for URL in URL_LIST:
        html_lists.append(scrap_page(URL))

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in html_lists:
            writer.writerow(row)
