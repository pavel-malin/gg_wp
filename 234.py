import socks
import socket
import random
import re
import datetime
import json
import os
import csv
from io import StringIO
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup







socks.set_default_proxy(socks.SOCKS5,"localhost", 9150,)
socket.sockets = socks.socksocket
print(urlopen('http://webprogramlife.ru').read())
service_args = ['--proxy=localhost:9150','--proxy-type=socks5']
driver = webdriver.PhantomJS(executable_path='<path to Phantom JS>',service_args = service_args)
driver.get("http://webprogramlife.ru")
print(driver.page_source)
driver.close()




html = urlopen("http://webprogramlife.ru")
bsObj = BeautifulSoup(html)

def main(self):
    languageName = "ru"
    FontName = "captchaFont"
    driverctory = '<path to images>'
    def runAll(self):
        self.createFontFeli()
        self.claenImages()
        self.extractUnicode()
        self.renameFiles()
        self.runShapeClustering()
        self.runMfTraining()
        self.runCnTrainig()
        self.createTestData()
