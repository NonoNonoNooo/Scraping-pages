import requests
from bs4 import BeautifulSoup
import xlsxwriter

headers = {
    'User-Agent':
    'Your User-Agent or the one you find'
}

url = "https://www.psychologicalsociety.ie/pd/?pd_s=&pd_d=&pd_areas_of_practice=&pd_language=Click%20search%20%E2%80%93%20you%20should"

responce = requests.get(url, headers=headers)

soup = BeautifulSoup(responce.text, 'lxml')

mane_div = soup.find_all('div', class_='find-psychologist-list')

def name():
    for i in mane_div:
        yield i.find('div', class_='name').text

def adres():
    for i in mane_div:
        if i.find('strong', text='Address:') != None:
            yield i.find('strong', text='Address:').find_previous().text[8:]
        else:
            yield "NONE"

def contact():
    for i in mane_div:
        if i.find('strong', text='Contact:') != None:
            yield i.find('strong', text='Contact:').find_previous().text[8:]
        else:
            yield "NONE"



book = xlsxwriter.Workbook(r'D:\document\finished\data\data.xlsx')
page = book.add_worksheet('data')

page.set_column('A:A', 50)
page.set_column("B:B", 50)
page.set_column('C:C', 50)

row = 0
colum = 0

for item in name():
    page.write(row, colum, item)
    row += 1

row = 0
colum = 1

for item in adres():
    page.write(row, colum, item)
    row += 1

row = 0
colum = 2

for item in contact():
    page.write(row, colum, item)
    row += 1

book.close()