# краулинг
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())
# Извлекаем список всех внутренних ссылок, найденных на странице
def getInternalLinks(bsObj, includeUrl):
    interanalLinks = []
# Находим все ссылки, которые начинаются с "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in interanalLinks:
                interanalLinks.append(link.attrs['href'])
                return interanalLinks
# Извлекаем список всех внешних ссылок, найденных на странице
            def getExternalLink(bsObj, excludeUrl, externalLinks=None):
                excludeUrl = []
# Находим все ссылки, которые начинаются с "http" или "www"
# Не содержит текучий Url-адрес
                for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
                    if link.attrs['href'] is not None:
                        if link.attrs['href'] not in externalLinks:
                            externalLinks.apped(link.attrs['href'])
                            return externalLinks
                        def splitAddress(address):
                            addressParts = address.replace("http://","").slipt("/")
                            return addressParts
                        def getRandomExternalLink(startingPage):
                            html = urlopen(startingPage)
                            bsObj = BeautifulSoup(html)
                            externalLinks = getExternalLink(bsObj,splitAddress(startingPage)[0])
                            if len(externalLinks) == 0:
                                interanalLinks = getInternalLinks(startingPage)
                                return externalLinks[random.randint(0,len(externalLinks)-1)]
                            def followExternalOnly(startingSite):
                                externalLinks = getRandomExternalLink("http://orelly,com")
                                print("Random external link is: "+externalLinks)
                                followExternalOnly("http://orelly.com")
# Добовлений функции
# Извлекаем список всех внешних URL-адресов, найденных на сайте
                                allExtLinks = set()
                                allIntLinks = set()
                                html = urlopen(SiteUrl)
                                bsObj = BeautifulSoup(html)
                                interanalLinks = getExternalLink(bsObj,splitAddress(siteUrl)[0])
                                externalLinks = getExternalLink(bsObj,splitAddress(sietUrl)[0])
                                for link in externalLinks:
                                    if link not in allExtLinks:
                                        allExtLinks.add(link)
                                        print(link)
                                        for link in interanalLinks:
                                            if link not in allIntLinks:
                                                print("about to get link: "+link)
                                                allIntLinks.add(link)
                                                getAllExternalLinks(link)
                                                getAllExternalLinks("http://oreilly.com")

