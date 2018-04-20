#!/usr/bin/env python3

import requests
import time
from bs4 import BeautifulSoup


#returns a list of tuples, with each tuple containing the stat along with the corresponding feature.
def return_stats(data):
    li = []
    values = data.find_all('div', class_='col-md-3 col-sm-4')
    for item in values:
        curr = list(item.children)
        print("Currently grabbing '%s' which has a value of '%s'" % (curr[3].get_text(),curr[1].get_text()))
        li.append((curr[3].get_text(),curr[1].get_text()));

#returns a list of tuples, one containing the player name, the other containing the list of tuples with stats.
def get_html():
  li = []
  website_base = 'https://fortnitestats.com/stats/'
  
  #need to find a way to convert between website names and user names

  player_list = ['domita7','staberrrrama','imso-sorry','nacnud556','Gemskillz','bricksey','eaze7','giladale','bluezberrymuffin']
  for player in player_list:
    print("Getting stats for player, '%s'" % (player))
    print("Waiting 2 seconds to request web page")
    time.sleep(2)
    page = requests.get(website_base + player)
    data = BeautifulSoup(page.content, 'html.parser')
    if not data:
        print("Data could not be found for this player")
        continue
    li.append((return_stats(data), player))
  return li

def main():
  all_stats = []
  all_stats = get_html()


if __name__ == "__main__":
    main()



