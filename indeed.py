
import os
import requests
from bs4 import BeautifulSoup
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

# def get_total_pages():
#     params={
#     "q":"kurir",
#     'l':"jakarta"
#     }
#     req=requests.get(url,params=params,headers=headers)
#     try:
#         os.mkdir("temp")

#     except FileExistsError:
#          pass   
#     with open('temp/res.html',"w+") as outfile:
#         outfile.write(req.text)
#         outfile.close()

#     soup=BeautifulSoup(req.text,'html.parser')
#     pagination=soup.find('ul','pagination-list')
#     pages=pagination.find_all('li')
#     list=[]
#     for page in pages:
#         list.append(page.text)
#     total =int(max(list))
#     print(total)
def get_job_list():
    params={
    "q":"kurir",
    'l':"jakarta"
    }
    req=requests.get(url,params=params,headers=headers)
    soup=BeautifulSoup(req.text,'html.parser')
    jobs=soup.find_all('table','jobCard_mainContent')
    list=[]
    for job in jobs:
        job_tiitle=job.find('h2','jobTitle').find('span').text
        job_company=job.find('span','companyName').text
        data_dict={
            'title':job_tiitle,
            'company_name':job_company
        }
        list.append(data_dict)

    print(list)  
if __name__ == "__main__":
    # get_total_pages()
    get_job_list()