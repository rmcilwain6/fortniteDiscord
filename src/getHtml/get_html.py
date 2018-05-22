# get_html and parseWebpage returns the parsed webpage data

import time
import requests
from bs4 import BeautifulSoup

class get_html:

    def __init__(self, playerName):
        self.url = 'https://fortnitestats.com/stats/' + playerName
        #self.playerName = playerName
        #self.websiteBase = 'https://fortnitestats.com/stats/'

    def parseWebpage(self):
        time.sleep(1)
        page = requests.get(self.url)
        if not page:
            print("Page could not be found for this player")
            exit(0)
        data = BeautifulSoup(page.content, 'html.parser')
        if not data:
            print("Data could not be found for this player")
            exit(0)
        return data
