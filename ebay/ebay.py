from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import json
import schedule
import time
from datetime import datetime



url='https://www.ebay.com/sch/i.html'
headers={ 'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
params={
    "_nkw":"laptop",
    "_ipg":"50" }

def get_details(link):
    req=requests.get(link,params=params)
    soup=BeautifulSoup(req.text,'html.parser')
    title_product=soup.find('h1',{'id':'itemTitle'}).find(text=True, recursive=False)
    try:
     total_sold=soup.find('div',{'id':'why2buy'}).find('div','w2b-cnt w2b-2 w2b-red').find('span','w2b-head').text+' sold'
    except AttributeError:
     total_sold='not found'
    condition=soup.find('div',{'id':'vi-itm-cond'}).text
    try:
     rating=soup.find('span','reviews-star-rating')['title'][0:3]
    except (TypeError,AttributeError):
     rating="rating not found" 
    price=soup.find('span',{'itemprop':'price'}).text
    image_link=soup.find('img',{'id':'icImg'})['src']
    data={
        "title_item": title_product,
        "total_sold":total_sold,
        "condition":condition,
        "rating":rating,
        'price':price,
        'image_link':image_link
    }

    return data

def get_product():
 now=datetime.now()      
 print(f'proggram run at {now}')

 req=requests.get(url,params=params)
 soup=BeautifulSoup(req.text,'html.parser')
 products=soup.find_all('li','s-item s-item__pl-on-bottom s-item--watch-at-corner')
 list=[]
 for product in products:
    link =product.find('a','s-item__link')['href']
    list.append(get_details(link))
 try:
     os.mkdir('json_result')
 except FileExistsError:
     pass 
   
 with open(f'json_result/data-created-{now.year}-{now.month}-{now.day}-{now.hour}:{now.minute}.json','w+') as json_data:
     json.dump(list,json_data)     
 print(f'data created at {now}') 
schedule.every(1).hours.do(get_product)

while True:
   schedule.run_pending()
   time.sleep(1)