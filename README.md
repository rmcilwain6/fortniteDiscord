# fortniteDiscord

Structure to hold all data:
    Dictionary{ 'name of player', {'name of field', value of field} }
    
    To get a value::
        dict_name['name of player']['name of field'] = 'value'

Layout:
    1. Grab list of users (list hardcoded in initially)
    2. For each user in list:
        a. Open up connection with fortnitestats.com
        b. Parse through HTML; scrape all data
        c. Compile data into a dictionary{'name of field', value of field}
        d. Return dictionary
    3. Append the returned dictionary to the main data structure for each user
