import requests
from bs4 import BeautifulSoup
import json
from twilio.rest import Client
import time
from datetime import datetime
from discord import *
from colorama import init, Fore, Back, Style
from os import system
from random import randrange

system('title ' + 'Louis Vuitton Monitor')

init(convert=True)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
           'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'en-GB,en;q=0.5',
           'Connection': 'keep-alive',
           'Content-Length': '1922',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Host': 'secure.louisvuitton.com',
           'Origin': 'https://uk.louisvuitton.com',
           'TE': 'Trailers'
           }

account_sid = 'AC7a2aa0f239453836298572fa8674924e'
auth_token = 'fd28cc380ea8dadd0a66a6c0b7f6cd5e'
client = Client(account_sid, auth_token)

productID=['M68241','M68272','N41207','M68242']#,'M47542']#,'M69119','M40712','M69136', 'N60286','M69269', 'M69137', 'N60359', 'N60359','M58009', 'N60286',]
urlwLinks={
    'M68272':'https://uk.louisvuitton.com/eng-gb/products/lv-chain-links-necklace-nvprod1630201v',
    'N41207':'https://uk.louisvuitton.com/eng-gb/products/pochette-accessoires-damier-azur-005868',
    'M68242':'https://uk.louisvuitton.com/eng-gb/products/monogram-colours-chain-bracelet-nvprod1630204v',
    'M68241':'https://eu.louisvuitton.com/eng-e1/products/monogram-colors-chain-necklace-nvprod1630203v',
    'M47542':'https://uk.louisvuitton.com/eng-gb/products/toiletry-pouch-26-monogram-canvas-000767',
    'M69119':'https://uk.louisvuitton.com/eng-gb/products/lv-escale-pochette-kirigami-nvprod2160054v',
    'M40712':'https://uk.louisvuitton.com/eng-gb/products/pochette-accessoires-monogram-005656',
    'M69136':'https://uk.louisvuitton.com/eng-gb/products/lv-escale-poche-toilette-26-nvprod2140067v#M69136',
    'M69137':'https://uk.louisvuitton.com/eng-gb/products/lv-escale-poche-toilette-26-nvprod2140067v#M69137',
    'M69269': 'https://uk.louisvuitton.com/eng-gb/products/lv-escale-mini-pochette-accessoires-nvprod2160048v',
    'N60359':'https://uk.louisvuitton.com/eng-gb/products/daily-card-holder-damier-azur-nvprod2090118v#N60359',
    'N60286':'https://uk.louisvuitton.com/eng-gb/products/daily-card-holder-damier-azur-nvprod2090118v#N60286',
    'M58009':'https://uk.louisvuitton.com/eng-gb/products/mini-pochette-accessoires-monogram-001025'

}
while (True):
    for i in range(len(productID)):
        url='https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=eng-gb&pageType=storelocator_section&skuIdList=' + productID[i]
        r=requests.get(url, headers=headers)
        jsonData=r.json()
        inStock=jsonData[productID[i]]['inStock']
        if inStock == False:
            dateTimeObj = datetime.now()
            print(Fore.CYAN + '[{}] item Not In Stock: {}'.format(str(dateTimeObj),productID[i]))
        else:

            prodtitle=productID[i]
            sendHook(prodtitle, urlwLinks[productID[i]])
            print(Fore.GREEN + '[{}] item In Stock: {}'.format(str(dateTimeObj),productID[i]))
        #    print('item in stock')
            #call = client.calls.create(
            #                twiml='<Response><Say>LV RESTOCK!</Say></Response>',
            #                to='+447876498559',
            #                from_='+441724410081'
            #            )
            #print(call.sid)
            #    message = client.messages.create(
        #            from_='+441724410081',
        #            body=productID[i] + ' changed instock status:' +urlwLinks[productID[i]],
        #            to='+447876498559')
        #    print(message.sid)