import get_html

if __name__=="__main__":
    player_list = ['domita7','staberrrrama','imso-sorry','nacnud556','gemskillz','bricksey','eaze7','giladale','bluezberrymuffin']
    for player in player_list:
        stats = get_html(player)