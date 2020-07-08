import requests
import json
import time,timeit
from datetime import datetime, timedelta
from threading import Timer

from modules import create_item, create_option, create_table, create_order, create_resto

from classes.Classes import Restaurant, Client

create_table()






def get_sleep_time():
    now = datetime.now()
    next_run = now.replace(minute=int(now.minute / 1) * 1, second=0, microsecond=0) + timedelta(minutes=1)
    return (next_run - now).total_seconds()

def dowork():
    now = datetime.now()
    print('Doing some work at', now)
    headers = {'Authorization': '4x5dsYmZhY5Vy6o3O'}
    r = requests.post("https://pos.globalfoodsoft.com/pos/order/pop", headers=headers)

    schedule_next_run()
    return r


def schedule_next_run():
    sleep_time = get_sleep_time()
    print(f'sleeping for {sleep_time} seconds')
    t = Timer(sleep_time, dowork)
    t.daemon = True
    t.start()



"""print('Starting work schedule')
schedule_next_run()
input('Doing work every 5 minutes. Press enter to exit')"""









def loaddata():
    for i in range(1):
        headers = {'Authorization': '4x5dsYmZhY5Vy6o3O'}
        r = requests.post("https://pos.globalfoodsoft.com/pos/order/pop", headers=headers)
    return r

reult1= loaddata()


dict_all = {'count': 1, 'orders': [{'instructions': None, 'coupons': [], 'tax_list': [], 'missed_reason': None, 'id': 97625569, 'total_price': 6500, 'sub_total_price': 5500, 'tax_value': 0, 'persons': 0, 'latitude': '14.682659756001303', 'longitude': '-17.440379392590327', 'client_first_name': 'Abdou', 'client_last_name': 'Ba', 'client_email': 'boumanga2015@gmail.com', 'client_phone': '+221777642995', 'restaurant_name': 'Bon Restaurant', 'currency': 'XOF', 'type': 'delivery', 'status': 'accepted', 'source': 'website', 'pin_skipped': False, 'accepted_at': '2020-04-29T22:53:06.000Z', 'tax_type': 'GROSS', 'tax_name': 'Sales tax', 'fulfill_at': '2020-04-29T23:23:06.000Z', 'reference': None, 'restaurant_id': 72530, 'client_id': 5284634, 'updated_at': '2020-04-29T22:53:06.000Z', 'restaurant_phone': '+221338222400', 'restaurant_timezone': 'Africa/Dakar', 'company_account_id': 591711, 'pos_system_id': 13613, 'restaurant_key': '4x5dsYmZhY5Vy6o3O', 'restaurant_country': 'Senegal', 'restaurant_city': 'Dakar', 'restaurant_zipcode': '11500', 'restaurant_street': "Rond point Jet d'eau", 'restaurant_latitude': '14.712147451727596', 'restaurant_longitude': '-17.455455226892127', 'restaurant_token': '0000', 'gateway_transaction_id': None, 'gateway_type': None, 'api_version': 2, 'payment': 'CASH', 'for_later': False, 'client_address': 'Central Park, Avenue Malick SY, 10500, Dakar', 'client_address_parts': {'street': 'Central Park, Avenue Malick SY', 'city': 'Dakar', 'more_address': '10500'}, 'items': [{'id': 118513401, 'name': 'DELIVERY_FEE', 'total_item_price': 1000, 'price': 1000, 'quantity': 1, 'instructions': None,

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'type': 'delivery_fee', 'type_id': None, 'tax_rate': 0, 'tax_value': 0, 'parent_id': None, 'item_discount': 0, 'cart_discount_rate': 0, 'cart_discount': 0, 'tax_type': 'GROSS', 'options': []}, {'id': 118513505, 'name': 'Pizza Prosciutto', 'total_item_price': 5000, 'price': 2500, 'quantity': 2, 'instructions': '', 'type': 'item', 'type_id': 1968216, 'tax_rate': 0, 'tax_value': 0, 'parent_id': None, 'item_discount': 0, 'cart_discount_rate': 0.5, 'cart_discount': 2500, 'tax_type': 'GROSS', 'options': [{'id': 124783655, 'name': 'Moyenne', 'price': 0, 'group_name': 'Taille', 'quantity': 1, 'type': 'size', 'type_id': 1221752}]}, {'id': 118513507, 'name': '50% de Remise', 'total_item_price': 0, 'price': 0, 'quantity': 1, 'instructions': None, 'type': 'promo_cart', 'type_id': 107013, 'tax_rate': 0, 'tax_value': 0, 'parent_id': None, 'item_discount': 5500, 'cart_discount_rate': 0.5, 'cart_discount': -5500, 'tax_type': 'GROSS', 'coupon': 'YXXBURNDDW0ZD', 'options': []}, {'id': 118513756, 'name': 'Spaghetti Bolognese', 'total_item_price': 4000, 'price': 4000, 'quantity': 1, 'instructions': 'Pas de piment!!', 'type': 'item', 'type_id': 1968217, 'tax_rate': 0, 'tax_value': 0, 'parent_id': None, 'item_discount': 0, 'cart_discount_rate': 0.5, 'cart_discount': 2000, 'tax_type': 'GROSS', 'options': []}, {'id': 118513945, 'name': 'Chicken Burger', 'total_item_price': 2000, 'price': 2000, 'quantity': 1, 'instructions': 'Piment !!', 'type': 'item', 'type_id': 3033467, 'tax_rate': 0, 'tax_value': 0, 'parent_id': None, 'item_discount': 0, 'cart_discount_rate': 0.5, 'cart_discount': 1000, 'tax_type': 'GROSS', 'options': []}]}]}
result = dowork()
resultats = result.json()
resultats2 = reult1.json()
print(resultats,resultats2)
commande_list = dict_all['orders']
# cmd = commande_list[0]

if commande_list == []:
    print('Il y a aucune commande')
else:
    for cmd in commande_list:
        resto = Restaurant(cmd['restaurant_id'], cmd['restaurant_name'], cmd['restaurant_phone'], cmd['restaurant_country'], cmd['restaurant_city'],
                           cmd['restaurant_street'], cmd['restaurant_latitude'], cmd['restaurant_longitude'], cmd['restaurant_token'], cmd['restaurant_zipcode'])

        resto.insertData()
        #restoId = create_resto(resto)
        #print(restoId, " resto iiii")

        cl = Client(cmd['client_id'], cmd['client_first_name'], cmd['client_last_name'],
                    cmd['client_email'], cmd['client_phone'], cmd['client_address'])
        cl.insertData()

        commande = (cmd['client_id'], cmd['restaurant_id'], cmd['total_price'], len(
            cmd['items']), cmd['type'], cmd['status'], cmd['source'], cmd['accepted_at'], cmd['fulfill_at'], cmd['instructions'], cmd['tax_value'], cmd['currency'], cmd['payment'])
        orderid = create_order(commande)
        print(orderid, 'cmd jdjdjdjdj')

        liste_articles = cmd['items']
    for article in liste_articles:
        # print(article['id'])

        item = [article['id'], article['name'], article['total_item_price'], article['price'],
                article['instructions'], article['type'], article['type_id'], article['item_discount'], article['cart_discount_rate'], article['cart_discount'], article['tax_type']]
        articleId = create_item(item)
        print (articleId, 'idddddd')

        liste_options = article['options']
        for option in liste_options:
            # print(option['id'])
            op = [option['name'], option['price'], option['group_name'],
                  option['quantity'], option['type'], option['type_id']]
            op_id = create_option(op)
            print(op_id, "gdgdgdgd")
