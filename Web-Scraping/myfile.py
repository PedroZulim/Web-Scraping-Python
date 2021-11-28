import requests
import re
from bs4 import BeautifulSoup

url='https://sarasotaavionics.com/'

headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

productlist=[]

r = requests.get('https://sarasotaavionics.com/category/autopilots?s=1000')
soup = BeautifulSoup(r.content,'lxml')

product = soup.find_all('h4', class_='product-name')
    
for item in product: 
    for ref in item.find_all('a', href = True):
        productlist.append(url + ref['href'])


for ref in productlist:
    r = requests.get(ref, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h2', class_='product-name').text.strip()
    avl = soup.find('span', class_='delivery-time').get('title').replace('Delivery time: ',"")
    part = soup.find(itemprop = 'mpn').get('content')
    aux = soup.find('div',class_="product-items").find_all('li')[2]
    cond = aux.text.strip().replace("Condition: ","")
   
    #PRICE -- mb itmprop? 28/11
    price = soup.find('span', class_="".text.strip)
    print(price)
    