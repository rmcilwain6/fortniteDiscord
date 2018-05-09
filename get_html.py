import time
from bs4 import BeautifulSoup

class get_html:

    websiteBase = 'https://fortnitestats.com/stats/'


    def __init__(self, player_name):
        self.player_name = player_name

    def parse_webpage(self):
        page = requests.get(websiteBase + player_name)
        data = BeautifulSoup(page.content, 'html.parser')
