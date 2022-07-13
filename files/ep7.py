# ep7
# web scraping

# pip install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

alldata = {}

def checktemp(ID):
    # url = 'https://www.tmd.go.th/province.php?id=37'
    url = 'https://www.tmd.go.th/province.php?id=' + str(ID)

    webopen = urlopen(url)
    html_page = webopen.read()
    webopen.close()
    # print(html_page)

    data = BeautifulSoup(html_page, 'html.parser')
    # print(data)

    try:
        # temp = data.find_all('td', {'class':'strokeme'})
        temp = data.find('td', {'class': 'strokeme'})
        title = data.find('span', {'class':'title'})
        # print(temp.text)
        # print(title.text.strip()) # .strip() uses for cutout whitespace in front and behide

        city = title.text.strip()
        temp = temp.text
        # print(city, temp)
        alldata[city] = temp
    except:
        # print('Could not find info you need')
        pass
# checktemp(37)

for i in range(1, 101):
    checktemp(i)

print(alldata)

def writetocsv(data):
    date = datetime.now().strftime('%Y%m%d')
    with open(f'data-temperature{date}.csv', 'a', newline='', encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)

for k, v in alldata.items():
    data = [k,v]
    writetocsv(data)