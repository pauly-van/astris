from bs4 import BeautifulSoup
from requests import get

def scrapeSlickDeals():
  url = 'https://slickdeals.net/'
  r = get(url)
  soup = BeautifulSoup(r.text, 'html.parser')

  # copied from https://github.com/MinweiShen/slickdeals/blob/master/slickdeals/utils.py
  removeHidden = soup.find_all('div', {'class': 'removeHidden'})
  fpdeals = []
  for r in removeHidden:
      fpdeals += r.find_all('div', {'class': 'frontpage'})
  deals = []

  for d in fpdeals:
      a = d.find('a', {'class': 'itemTitle'})
      link = SLICKDEALS + a['href']
      price_line = d.find('div', {'class': 'priceLine'})
      title = price_line['title']
      price_div = price_line.find('div', {'class': 'itemPrice'})
      price = price_div and price_div.getText().strip() or 'None'
      shipinfo_div = price_line.find('div', {'class': 'priceInfo'})
      shipinfo = shipinfo_div and shipinfo_div.getText().strip() or 'None'
      item = {
          'title': title,
          'link': link,
          'price': price,
          'info': shipinfo
      }
      if show_free_price:
          if 'free' in price.lower():
              deals.append(item)
      elif show_free:
          if 'free' in shipinfo.lower() or 'free' in price.lower():
              deals.append(item)
      else:
          deals.append(item)

  return deals