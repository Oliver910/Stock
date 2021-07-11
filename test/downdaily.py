import requests
import re
import csv
from operator import itemgetter, attrgetter

"""
試寫注解
"""

def getFilename_fromCd(cd):
    if not cd:
        return None
    print(cd)
    fname = re.findall('filename="(.+)"', cd)
    if len(fname) == 0:
        return None
    
    return fname[0]


url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'

r = requests.get(url, allow_redirects=True)
filename = getFilename_fromCd(r.headers.get('content-disposition'))
print(filename)

open(filename, 'wb').write(r.content)

csvdata=[]

with open(filename, newline='', encoding = 'utf8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if row[0] != '證券代號':
            if row[4]=="":
                ov = 0.0;
            else:
                ov = (float(row[8])/float(row[4]))
            row.append(ov)            
            csvdata.append(row)


def sortSecond(val):
    return val[10]

csvdata.sort(key = sortSecond , reverse = True) 

for row in csvdata[:50] :
    print(row)
    
    