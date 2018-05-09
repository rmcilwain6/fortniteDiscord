#!/usr/bin/env python3

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = 'https://fortnitestats.com/stats/imso-sorry'
#stats = 'card-body'

def main():
    #opening up connection, grabbing page
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    #html parsing
    page_soup = soup(page_html, "html.parser")

    #container holds each header and the data within
    container = page_soup.find("div",{"class":"col-md-8"})

    headers = [header.get_text().strip() for header in container.findAll("div",{"class":"card-header"})]
    
    # a list of the HTML cards containg different categories of stats
    card_bodys = container.find_all("div",{"class":"card-body"})

    card = {header: 0 for header in headers}
    for header,card_body in zip(headers,card_bodys):
        stats = [stat.get_text() for stat in card_body.find_all('p')]
        values = [val.get_text() for val in card_body.find_all('h4')]
        stat_val = list(zip(stats,values))
        card[header] = stat_val

    print("Dictionary:\n")
    print(card.items())
    for (header,vals) in card.items():
        print(header)
        print(vals)
        print()

if __name__ == "__main__":
    main()