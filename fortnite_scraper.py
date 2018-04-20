#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def main():
  website = "https://fortnitestats.com/stats/domita7"
  print(website)
  #website_to_stats = 'https://fortnitestats.com/stats/'
  #print(website)
  #page = urllib2.urlopen(website)
  page = requests.get(website)
  #print(page.content)
  player_list = ['domita7','staberrrrama','ImSo_Sorry','Nacnud556','Gemskillz','Bricksey','Eaze7','Giladale','BluezBerryMuffin']
  print(player_list)
  data = BeautifulSoup(page.content, 'html.parser')
  #print(data.prettify())
  #for item in data.children:
  #  print(type(item))
  #print(data);
  #print(data.children[0].children)
  values = data.find_all('div', class_='col-md-3 col-sm-4')
  for item in values:
      curr = list(item.children)
      #print(curr[3].get_text(strip=True))
      if curr[3].get_text() in "K/D Ratio":
        print(curr[1].get_text())



if __name__ == "__main__":
    main()



