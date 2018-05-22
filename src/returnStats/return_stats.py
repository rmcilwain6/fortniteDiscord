import re

class return_stats:

    def __init__(self, data):
        self.data = data

    def storeStats(self):
        container = self.data.find("div",{"class":"col-md-8"})
        headers = [header.get_text().strip() for header in container.findAll("div", {"class":"card-header"})]
        card_bodys = container.find_all("div",{"class":"card-body"})
        header_li = []
        stat_dict = {}
        for header in headers:
            new_header = re.sub("(\w)*$", "", header)
            header_li.append(new_header)
        for header,card_body in zip(headers,card_bodys):
            stats = [stat.get_text() for stat in card_body.find_all('p')]
            if header not in "Overall Stats":
                stats = [header + stat for stat in stats]
            values = [val.get_text() for val in card_body.find_all('h4')]
            new_value_list = []
            for val in values:
                new_value = re.sub("[^\d\.]", "", val)
                new_value_list.append(new_value)
            stat_val = list(zip(stats,new_value_list))
            for (stat,value) in stat_val:
                stat_dict[stat] = value
        #print(stat_dict)
        return stat_dict

            