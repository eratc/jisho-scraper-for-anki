import requests
from bs4 import BeautifulSoup


def parse_kanji(kanji_soup):
    kanji_details = kanji_soup.find('div', attrs={'class': 'kanji details'})
    main_readings = kanji_details.find('div', attrs={'class': 'kanji-details__main-readings'})

    kun_list = []
    on_list = []

    kun_yomi = main_readings.find('dl', attrs={'class': 'dictionary_entry kun_yomi'})
    on_yomi = main_readings.find('dl', attrs={'class': 'dictionary_entry on_yomi'})

    if kun_yomi:
        for a in kun_yomi.find_all('a'):
            kun_list.append(a.string)
            a.unwrap()

    if on_yomi:
        for a in on_yomi.find_all('a'):
            on_list.append(a.string)
            a.unwrap()

    return ['、　'.join(kun_list), '、　'.join(on_list)]


def scrap_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find('div', id='page_container')

    kanji = result.find('h1', attrs={'class': 'character'}).getText(strip=True)
    description = result.find('div', attrs={'class': 'kanji-details__main-meanings'}).getText(strip=True)
    jlpt = result.find('div', attrs={'class': 'jlpt'})

    if jlpt:
        jlpt = jlpt.find('strong').getText(strip=True)
    else:
        jlpt = ''

    print(kanji)

    kanji_soup_list = parse_kanji(result)
    return [kanji, description] + kanji_soup_list + [jlpt, url]
