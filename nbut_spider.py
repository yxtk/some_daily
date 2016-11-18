import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
jobs = client['jobs']
sheet_line = jobs['sheet_line']

for i in range(1, 32):
    urls = ['http://nbut.jysd.com/campus/index?page={}'.format(i)]
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')

        titles = soup.select('div > ul > li.span7 > a')
        places = soup.select('div > ul > li.span1')
        times = soup.select('div > ul > li.span4')

        for title,place,time in zip (titles,places,times):
            data = {
                'title':title.get_text(),
                'place':place.get_text(),
                'time':time.get_text()
            }
            print(data)
            sheet_line.insert_one(data)
print("已全部抓取并存储")









