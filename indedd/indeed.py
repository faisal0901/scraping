
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
url='https://id.indeed.com/lowongan-kerja?'
params={
    "q":"kurir",
    'l':"jakarta"

}
headers={
    'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
req=requests.get(url,params=params,headers=headers)
soup=BeautifulSoup(req.text,'html.parser')

def get_total_pages(query,location,start):
    params={
    "q":query,
    'l':location,
    "start":start
    }
    req=requests.get(url,params=params,headers=headers)
    try:
        os.mkdir("temp")

    except FileExistsError:
         pass   
    with open('temp/res.html',"w+") as outfile:
        outfile.write(req.text)
        outfile.close()

    soup=BeautifulSoup(req.text,'html.parser')
    pagination=soup.find('ul','pagination-list')
    pages=pagination.find_all('li')
    list=[]
    for page in pages:
        list.append(page.text)
    total =int(max(list))
    print(total)
def get_job_list(query,location,start):
    params={
    "q":query,
    'l':location,
    "start":start
    }
    req=requests.get(url,params=params,headers=headers)
    soup=BeautifulSoup(req.text,'html.parser')
    jobs=soup.find_all('table','jobCard_mainContent')
    list=[]
    for job in jobs:
        job_tiitle=job.find('h2','jobTitle').find('span',{"title":True}).text
        job_company=job.find('span','companyName').text
        print(job_tiitle)
        data_dict={
            'title':job_tiitle,
            'company_name':job_company
        }
        list.append(data_dict)
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass      
    with open(f'json_result/{query}_in_{location}_page_{start}.json','w+') as json_data:
     json.dump(list,json_data)    
    df=pd.DataFrame(list)
    df.to_csv('inded_data.csv',index=False)
    df.to_excel('inded_data.xlsx',index=False)

    print('data created')
def run():
     pass   
if __name__ == "__main__":
    # get_total_pages()
    get_job_list("python","jakarta",20)