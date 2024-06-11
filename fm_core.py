import fm_model_db as db
import fm_dist

"""
        This is standart data sequence for most functions (for each market)
        0 - fmid 
        1 - marketname
        2- state
        3 - zip
        4 - m.x
        5 - m.y
        1021746, 'Perry County Farmers Market Perryville', 'Arkansas', '72126', -92.801421, 35.005134
"""


def search_rad(markets, mrkt_srch, raduis_km):
    search_point = (mrkt_srch[4], mrkt_srch[5])
    markts_search = []
    for market in markets:
        point2 = (market[4], market[5])
        if fm_dist.calculate_distance(search_point, point2) < raduis_km:
            if market[0] != mrkt_srch[0]:
                markts_search.append(market)
    return markts_search


def convert_fullinfo(market):
    """
    Function converts total info about current market to a readable format.
    Original data consists of the following values:
    0 - fmid int NOT NULL,
    1 - marketname varchar(255),
    2 - website varchar(255),
    3 - facebook varchar(255),
    4 - twitter varchar(255),
    5 - youtube varchar(255),
    6 - othermedia varchar(255),
    7 - street varchar(255),
    8 - city varchar(255),
    9 - county varchar(255),
    10 - state varchar(255),
    11 - zip varchar(5),
    12 - season1date varchar(255),
    13 - season1time varchar(255),
    14 - season2date varchar(255),
    15 - season2time varchar(255),
    16 - season3date varchar(255),
    17 - season3time varchar(255),
    18 - season4date varchar(255),
    19 - season4time varchar(255),
    20 - x float,
    21 - y float,
    22 - location varchar(255),
    23 - credit CHAR(1),
    24 - wic CHAR(1),
    25 - wiccash CHAR(1),
    26 - sfmnp CHAR(1),
    27 - snap CHAR(1),
    28 - organic CHAR(1),
    29 - bakedgoods CHAR(1),
    30 - cheese CHAR(1),
    31 - crafts CHAR(1),
    32 - flowers CHAR(1),
    33 - eggs CHAR(1),
    34 - seafood CHAR(1),
    35 - herbs CHAR(1),
    36 - vegetables CHAR(1),
    37 - honey CHAR(1),
    38 - jams CHAR(1),
    39 - maple CHAR(1),
    40 - meat CHAR(1),
    41 - nursery CHAR(1),
    42 - nuts CHAR(1),
    43 - plants CHAR(1),
    44 - poultry CHAR(1),
    45 - prepared CHAR(1),
    46 - soap CHAR(1),
    47 - trees CHAR(1),
    48 - wine CHAR(1),
    49 - coffee CHAR(1),
    50 - beans CHAR(1),
    51 - fruits CHAR(1),
    52 - grains CHAR(1),
    53 - juices CHAR(1),
    54 - mushrooms CHAR(1),
    55 - petfood CHAR(1),
    56 - tofu CHAR(1),
    57 - wildharvested CHAR(1),
    58 - updatetime varchar(255)

    Items that got raw from DB (sequence as written)
    1 - marketname varchar(255),
    7 - street varchar(255),
    8 - city varchar(255),
    9 - county varchar(255),
    10 - state varchar(255),
    11 - zip varchar(5),
    20 - x float,
    21 - y float,
    Next raws transformed from raw Y/N to related strings
    starting from index 28 to 57 (29 rows)
    """
    goods = ['organic',
             'bakedgoods',
             'cheese',
             'crafts',
             'flowers',
             'eggs',
             'seafood',
             'herbs',
             'vegetables',
             'honey',
             'jams',
             'maple',
             'meat',
             'nursery',
             'nuts',
             'plants',
             'poultry',
             'repaired',
             'soap',
             'trees',
             'wine',
             'coffee',
             'beans',
             'fruits',
             'grains',
             'juices',
             'mushrooms',
             'petfood',
             'tofu',
             'wildharvested']
    convertedinfo = []
    convertedinfo.append(market[1])
    convertedinfo.append(market[7])
    convertedinfo.append(market[8])
    convertedinfo.append(market[9])
    convertedinfo.append(market[10])
    convertedinfo.append(market[11])
    convertedinfo.append(market[20])
    convertedinfo.append(market[21])
    dbindex = 28
    for product in goods:
        if market[dbindex] == "Y":
            convertedinfo.append(product)
        dbindex = dbindex + 1
    return convertedinfo



#data = db.show_all()
#market1 = (1021746, 'Perry County Farmers Market Perryville', 'Arkansas', '72126', -92.801421, 35.005134, None)
#market2 = db.market_full_info(1021746)
#print(market2)
#print(convert_fullinfo(market2))
#print(search_rad(data, market1, 50))