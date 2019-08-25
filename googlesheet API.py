# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:11:32 2019

@author: Dai
"""

import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))

for index, item in enumerate(dcard_title[:1]):
    #print("{0:2d}. {1}".format(index + 1, item.text.strip()))
    
    print('前20大熱門Dcard文章已寫入')

#寫入試算表內

import sys
import json
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#authorize_path
GDriveJSON_path = 'python-230518-9f6b02dba966.json'

scopes = ["https://spreadsheets.google.com/feeds"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(GDriveJSON_path , scopes)

gss_client = gspread.authorize(credentials)

#存取Google sheet"UploadPython"
gspreadsheet_key = '1xwGIyWQtHq_v_sTDGjVzKW-rcIkz_FeNJoprj7zFirc'

sheet = gss_client.open_by_key(gspreadsheet_key).sheet1

'''for index, item in enumerate(dcard_title[:20]):
    
    listt = index+1,"{1}".format(index + 1, item.text.strip())

    sheet.append_row(listt)'''


listt = '123','456','789'
sheet.append_row(listt)




