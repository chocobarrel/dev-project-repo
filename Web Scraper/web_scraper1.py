from bs4 import BeautifulSoup
from pip._vendor import requests

print("Web Scraper for Itemku.com product")
print()

url = input("Input URL : ")
print()

page = requests.get(url)
doc = BeautifulSoup(page.content,"html.parser")

section =doc.find("div", class_="flex flex-col leading-tight")
item_name = section.find("h1", class_="font-bold text-nero relative undefined text-xl leading-6")
price = section.find("h2", class_="text-3xl text-persimmon font-bold mr-2")
item_stock = section.find("p", class_="h-4 leading-normal self-center table align-middle")

print(item_name.text)
print(price.text)
print(item_stock.text)