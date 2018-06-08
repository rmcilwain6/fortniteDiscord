# get_html and parseWebpage returns the parsed webpage data

import time
import requests
from bs4 import BeautifulSoup

class get_html:

    def __init__(self, playerName):
        self.playerName = playerName
        self.url = 'https://fortnitestats.com/stats/' + playerName

    def parseWebpage(self):
        print("Waiting 1 second before getting html data for: " + self.playerName)
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
