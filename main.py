import sqlite3
from bs4 import BeautifulSoup
import urllib.request
import sys

url = "http://safar.tropmet.res.in/ahmedabad.php?city_id=&for=forecast_tomorrow"

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")
    sys.exit(1)

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

scripts = soup.find_all('script')
print(len(scripts))
# print(scripts[14])
soup = scripts[14]
import pdb; pdb.set_trace()
data = soup.text.replace("var markers =","").replace("} ];", "} ]")
# .replace("\r","").replace("\t","").replace("\n","").replace("\'",'"')



import json
data2 = json.loads(data)



