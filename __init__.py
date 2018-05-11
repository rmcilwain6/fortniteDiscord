#!/usr/bin/env python3

from getHtml.get_html import get_html
from returnStats.return_stats import return_stats

if __name__=="__main__":
    player_list = ['domita7','staberrrrama','imso-sorry','nacnud556','gemskillz','bricksey','eaze7','giladale','bluezberrymuffin']
    for player in player_list:
        stats = get_html(player)
        data = stats.parseWebpage()
        #print(data)
        #At this point, stats.parseWebpage() returns the BeautifulSoup parsed html. 
        temp = return_stats(data)
        new_dict = temp.storeStats()
