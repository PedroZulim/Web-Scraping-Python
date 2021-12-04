import requests
import pandas as pd
from bs4 import BeautifulSoup

def funcprice(price):
    if price:
        return (price['content'])
    else:
        return (0)
    
url='https://sarasotaavionics.com/'

headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

productlist = []
produtolist = []

r = requests.get('https://sarasotaavionics.com/category/autopilots?s=300')
soup = BeautifulSoup(r.content,'lxml')

product = soup.find_all('h4', class_='product-name')
    
for item in product: 
    for ref in item.find_all('a', href = True):
        productlist.append(url + ref['href'])


for ref in productlist:
    r = requests.get(ref, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    name = soup.find('h2', class_ = 'product-name').text.strip()
    
    avl = soup.find('span', class_ = 'delivery-time').get('title').replace('Delivery time: ',"")
    
    part = soup.find(itemprop = 'mpn').get('content')
    
    auxcond = soup.find('div',class_ = "product-items").find_all('li')[2]
    cond = auxcond.text.strip().replace("Condition: ","")
    
    price = soup.find('meta', itemprop = 'price')
    auxprice = funcprice(price)
    
    test = []
    optionlist = []
    option = soup.find_all('option', value = True)
    for option in option:
        optionlist.append(option.text.strip())
    if optionlist:
        test = (';'.join(optionlist))
    else:
        test = "N/A"

    produto = {
        'Name' : name,
        'Aviability' : avl,
        'Part_No' : part,
        'Condition' : cond,
        'Price' : auxprice,
        'Options' : test
    }
    produtolist.append(produto)
        
df = pd.DataFrame(produtolist)
df.to_csv('teste.csv', sep = ';', encoding = 'utf-8', index = False, header = True)