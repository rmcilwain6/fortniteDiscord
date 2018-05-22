import re

class return_stats:

    def __init__(self, data):
        self.data = data

    def storeStats(self):
        container = self.data.find("div",{"class":"col-md-8"})
        headers = [header.get_text().strip() for header in container.findAll("div", {"class":"card-header"})]
        card_bodys = container.find_all("div",{"class":"card-body"})
        #print(headers)
        #print(card_bodys)