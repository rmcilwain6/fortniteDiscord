#!/usr/bin/env python3

import requests
import time
import re
from operator import itemgetter
from bs4 import BeautifulSoup


#returns a list of tuples, with each tuple containing the stat along with the corresponding feature.
def return_stats(data):
  li = []
  box_prefix = ['Solo','Duo','Squad']
  boxes = data.find_all('div', class_='card-body')
  counter = 0
    #boxes returns a list which holds each occurence of the card-body class. There we should see 6 items.
  for box in boxes[2:]:
    #print("-----------------\n")
    values = box.find_all('div', class_='col-md-3 col-sm-4')
    if counter is 0:
      #case for overall stuff
      for item in values:
        curr = list(item)
        new_value = curr[1].get_text()
        new_value = re.sub("[^\d\.]", "", new_value)
        if curr[3].get_text() is "":
          li.append(("Overall Winrate", float(new_value)))
          continue
        li.append((curr[3].get_text(), float(new_value)))
    else:
      for item in values:
        curr = list(item)
        #print(curr)
        #This gets rid of commas and percent signs (and anything else) so we can convert the value from a string to a float so it can be sorted.
        new_value = curr[1].get_text()
        new_value = re.sub("[^\d\.]", "", new_value)
        #print(new_value)
        #print(type(new_value))
        #print(curr[3].get_text())
        if curr[3].get_text() is "":
          li.append((box_prefix[counter-1]+"Winrate", float(new_value)))
          continue
        li.append((box_prefix[counter-1]+curr[3].get_text(), float(new_value)))
        #print(type(item))
        #print("Currently grabbing '%s' which has a value of '%s'" % (curr[3].get_text(),curr[1].get_text()))
    counter = counter + 1
  #print(li)
  return li

#returns a list of tuples, one containing the player name, the other containing the list of tuples with stats.
def get_html():
  li = []
  website_base = 'https://fortnitestats.com/stats/'
  
  #need to find a way to convert between website names and user names

  player_list = ['domita7','staberrrrama','imso-sorry','nacnud556','gemskillz','bricksey','eaze7','giladale','bluezberrymuffin']
  for player in player_list:
    print("Getting stats for player, '%s'" % (player))
    print("Waiting 1 seconds to request web page")
    time.sleep(1)                                         #only want to scrape the website so often so we dont look suspicious, this waits one second
    page = requests.get(website_base + player)
    data = BeautifulSoup(page.content, 'html.parser')   #data is the parsed webpage, its a beautifulsoup object that we pass
    if not data:                                          #makes sure data is not null
        print("Data could not be found for this player")
        continue
    li.append((return_stats(data), player))
  #print(li)
  return li

def sort_stat(li, stat):
  sort_li = []
  for (list_of_stats, player) in li:
    #print("Currently looking for the stats for: %s" % (player))
    for (name, value) in list_of_stats:
      #print(name)
      #print(value)
      #print("Comparing '%s' and '%s'" % (name, stat))
      if name in stat and name in stat:
        #print("Succesful match!")
        sort_li.append((value, player))
  #print("List before sort:")
  #print(sort_li)
  sort_li.sort(key=itemgetter(0), reverse=True)
  #print("List after sort")
  #print(sort_li)
  return sort_li

def main():
  all_stats = []
  all_stats = get_html()
  print(all_stats)
  #So right here we have a list of tuples, containing the name of the player, and their stats.
  print(sort_stat(all_stats, 'Total Kills'))
  print(sort_stat(all_stats, 'Overall KD'))
  print(sort_stat(all_stats, 'Total Wins'))




if __name__ == "__main__":
    main()



