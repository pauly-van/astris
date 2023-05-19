#! /usr/bin/python3
from bs4 import BeautifulSoup
from requests import get

async def scrapeSlickDeals():
    url = 'https://slickdeals.net'
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    removeHidden = soup.find_all('li', {'class': 'frontpageGrid__feedItem'})

    fpdeals = []
    for r in removeHidden:
        fpdeals += r.find_all('div', {'data-module-id': 'Frontpage Slickdeals'})
    deals = []
    print(fpdeals)

    for d in fpdeals:
        card_content = d.find('div', {'class': 'dealCard__content'})
        title = card_content.find('a', {'class': 'dealCard__title'})
        price = card_content.find('span', {'class': 'dealCard__price'})

        item = {
          'title': title.text,
          'price': price.text if price else None,
          'link': url + title['href'] if title['href'] else None,
        }
        deals.append(item)

    return deals


