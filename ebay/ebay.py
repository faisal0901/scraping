


from bs4 import BeautifulSoup
import requests

url='https://www.ebay.com/sch/i.html'
header={ 'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
params={
    "_nkw":"laptop",
    "_ipg":"50"
}
req=requests.get(url,params=params,headers=header)
soup=BeautifulSoup(req.text,'html.parser')

def get_details(link):
    print(link)
    req=requests.get(link,params=params,headers=header)
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
    
 
    print("title item : ",title_product.encode('utf-8-sig'))
    print("total_sold :",total_sold)
    print("condition : ",condition)
    print("rating :",rating)
    print('price: ',price)
# get_details("https://www.ebay.com/itm/185263054311?hash=item2b2289dde7:g:VUsAAOSwaQZh5xQJ")
products=soup.find_all('li','s-item s-item__pl-on-bottom s-item--watch-at-corner')
counter=0
for product in products:
    link =product.find('a','s-item__link')['href']
    get_details(link)




