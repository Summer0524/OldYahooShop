address = input('輸入網址: ')
tota = input('輸入商品總數: ')

import pymysql

db = pymysql.connect("140.136.148.218","dbteam","878787","test", charset='utf8')

cur = db.cursor()

import requests
from bs4 import BeautifulSoup
nxtpg = ('hello')
i=0
ids = 1549

total = (int)(tota)
pag = (total-3)/24
page = (int)(pag)

if page == 0:
    lastotal = total
if total < 4:
    lastotal = 0

if page>0 and (total-3)%24 == 0:
    page = page-1

tagname = ('camera')

res = requests.get(address)
soup = BeautifulSoup(res.text, "html.parser")

for x in range(3):
        reup = soup.select('.pdlsit-main.yui3-u')[x]
        print( reup.select('.yui3-u-1.name')[0].text)
        name = reup.select('.yui3-u-1.name')[0].text
        print("$",reup.select('.yui3-u.pd-price span.nums')[0].text)
        price = (int)(reup.select('.yui3-u.pd-price span.nums')[0].text)
        print(reup.findAll('a')[0].get('href'))
        link = reup.findAll('a')[0].get('href')
        print(reup.findAll('img')[0].get('src'))
        Plink = reup.findAll('img')[0].get('src')
        print(ids)
        print()
        dbdata = [ids, name, price, link, Plink, tagname]
        cur.execute("INSERT INTO test2(id, name, price, link, pic, tag) VALUES(%s, %s, %s, %s, %s, %s)", dbdata)
        i = i+1
        ids = ids+1


for m in range(page):
    x=0
    nextpage2 = 1
    nextpage1 = 0
    if page>9:
        nextpage2 = 2
        nextpage1 = 1
    if m>9 and page >19 and m<(page-(page%10)):
        nextpage2 = 3

    for x in range(24):
        if x==0 and m!=0:
            res = requests.get("https://tw.buy.yahoo.com/"+nxtpg)
            soup = BeautifulSoup(res.text, "html.parser")

            
            reup = soup.select('.neighbor.yui3-u')[nextpage2]

            
            nxtpg = reup.findAll('a')[0].get('href')
        if m==0 and x==0:
            reup = soup.select('.neighbor.yui3-u')[nextpage1]

            
            nxtpg = reup.findAll('a')[0].get('href')
            
        reup = soup.select('.yui3-u-1-4')[x]
        print( reup.select('.yui3-u-1.name')[0].text)
        name = reup.select('.yui3-u-1.name')[0].text
        print("$",reup.select('.yui3-u-1.pd-price span.nums')[0].text)
        price = (int)(reup.select('.yui3-u-1.pd-price span.nums')[0].text)
        print(reup.findAll('a')[0].get('href'))
        link = reup.findAll('a')[0].get('href')
        print(reup.findAll('img')[0].get('_src'))
        Plink = reup.findAll('img')[0].get('_src')
        print(ids)
        print()

        dbdata = [ids, name, price, link, Plink, tagname]
        cur.execute("INSERT INTO test2(id, name, price, link, pic, tag) VALUES(%s, %s, %s, %s, %s, %s)", dbdata)
        
        i = i+1
        ids = ids+1
    res = requests.get("https://tw.buy.yahoo.com/"+nxtpg)
    soup = BeautifulSoup(res.text, "html.parser")


lastotal = total-i


for z in range(lastotal):

        reup = soup.select('.yui3-u-1-4')[z]
        print( reup.select('.yui3-u-1.name')[0].text)
        name = reup.select('.yui3-u-1.name')[0].text
        print("$",reup.select('.yui3-u-1.pd-price span.nums')[0].text)
        price = (int)(reup.select('.yui3-u-1.pd-price span.nums')[0].text)
        print(reup.findAll('a')[0].get('href'))
        link = reup.findAll('a')[0].get('href')
        print(reup.findAll('img')[0].get('_src'))
        Plink = reup.findAll('img')[0].get('_src')
        print(ids)
        print()

        dbdata = [ids, name, price, link, Plink, tagname]
        cur.execute("INSERT INTO test2(id, name, price, link, pic, tag) VALUES(%s, %s, %s, %s, %s, %s)", dbdata)
        
        i = i+1
        ids = ids+1


cur.close()
db.commit()
db.close() 

print("done")


        
    




