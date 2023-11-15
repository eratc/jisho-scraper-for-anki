import requests
import csv
from bs4 import BeautifulSoup


def scrap_page(url):
    # Example link: 'https://jisho.org/search/%23kanji %23jinmei'
    result = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get all kanji on page
    kanji_spans = soup.find_all('span', attrs={'class': 'character literal japanese_gothic'})

    for span in kanji_spans:
        result.append(span.a['href'])

    if next_page := soup.find('a', attrs={'class': 'more'}):
        print(next_page['href'])
        return result + scrap_page('https:' + next_page['href'])
    else:
        return result


def list_kanji_from_search(url, output_path):
    kanji_str_list = scrap_page(url)

    print(len(kanji_str_list))
    print(kanji_str_list)

    with open(output_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for kanji in kanji_str_list:
            writer.writerow(['https:' + kanji])



