import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
def sendMail(subject,body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "chrismas_alerts@pythonscraping.com"
    msg['To'] = "ryan@pythonscraping.com"
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
    while(bsObj.find("a",{"id":"answer"}).attrs['title']=='NO'):
        print("It is not Christmas get.")
        time.sleep(3600)
        bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
        sendMail("It's Christmas!", "Acconding to http://itischristmas.com, it is Christmas!")
        return

