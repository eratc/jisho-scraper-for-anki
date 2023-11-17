import requests
from verb_inflections import *
from bs4 import BeautifulSoup

LINK_PREFIX = 'https://jisho.org/search/'


def get_inflections(text, pos):
    vrb = V1(text, "v1", "") if pos == 'v1' else Godan(text, pos, "")
    return [text,
            vrb.non_past_p(), vrb.non_past_n(),
            vrb.masu_p(), vrb.masu_n(),
            vrb.past_p(), vrb.past_n(),
            vrb.past_polite_p(), vrb.past_polite_n(),
            vrb.te_p(), vrb.te_n(),
            vrb.potential_p(), vrb.potential_n(),
            vrb.passive_p(), vrb.passive_n(),
            vrb.causative_p(), vrb.causative_n(),
            vrb.causative_passive_p(), vrb.causative_passive_n(),
            vrb.imperative_p(), vrb.imperative_n()]


def scrap_page(url, pos):
    result = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    verb_divs = soup.find_all('div', attrs={'class': 'concept_light clearfix'})

    for div in verb_divs:
        verb_div = div.find_next('div', attrs={'class': 'concept_light-representation'})
        link = verb_div.find_next('a', attrs={'class': 'light-details_link'})
        span = verb_div.find_next('span', attrs={'class': 'text'})
        text = span.get_text(strip=True)
        inflections = get_inflections(text, pos)
        inflections.append(pos)
        inflections.append(f"https:{link['href']}")
        result.append(inflections)

    if next_page := soup.find('a', attrs={'class': 'more'}):
        print(next_page['href'])
        return result + scrap_page('https:' + next_page['href'], pos)
    else:
        return result


def search_all(args):
    result = []
    for pos in args.verb_pos:
        for tag in args.verb_search_tags:
            url = f"{LINK_PREFIX}%23{tag} %23{pos}"
            print('url: ', url)
            result.extend(scrap_page(url, pos))

    return result
