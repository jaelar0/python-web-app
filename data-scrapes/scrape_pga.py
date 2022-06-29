import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrapePga(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', id = 'statsTable')
    header = table.find('thead')
    body = table.find('tbody')
    rows = body.find_all('tr')
    col_num = len(header.find_all('th'))
    
    col_list = []
    i = 0
    while i < col_num:
        col_list.append(header.find_all('th')[i].text.strip())
        i = i + 1
    data_dict = {k: [] for k in col_list}

    j = 0
    while j < col_num:
        for row in rows:
            data_dict[col_list[j]].append(row.find_all('td')[j].text.strip())
        j = j + 1

    return data_dict
