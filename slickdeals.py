from bs4 import BeautifulSoup
from requests import get

def scrapeSlickDeals():
    url = 'https://slickdeals.net'
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    removeHidden = soup.find_all('div', {'class': 'removeHidden'})

    fpdeals = []
    for r in removeHidden:
        fpdeals += r.find_all('li', {'data-module-id': 'Frontpage Slickdeals'})
    deals = []

    for d in fpdeals:
        card_content = d.find('div', {'class': 'bp-c-card_content'})
        title = card_content.find('a', {'class': 'bp-c-card_title'})
        price = card_content.find('span', {'class': 'bp-p-dealCard_price'})

        item = {
          'title': title.text,
          'price': price.text if price else None,
          'link': url + title['href'] if title['href'] else None,
        }
        deals.append(item)

    return deals