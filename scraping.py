from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.vk.com")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll(text="prince")
for name in nameList:
    print(len(nameList))

# keyword пример
# allText = bsObj.findAll(id="text")
# print(allText[0].get_text())


# проверяет только по title, h
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup

# def getTitle(url):
  #  try:
   #     html = urlopen(url)
   # except HTTPError as e:
   #     return None
   # try:
    #    bsObj = BeautifulSoup(html.read())
    #    title = bsObj.body.h1
    # except AttributeError as e:
      #  return None
    # return title
# title = getTitle("http://www.facebook.com")
# if title == None:
  #  print("Title could not be found")
# else:
  #  print(title)
# начала
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# bsObj = BesutitulSoup(html.read())
# print(bsObj)
