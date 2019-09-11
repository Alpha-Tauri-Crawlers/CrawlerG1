# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

#url coletada pelo robo
url = str("https://g1.globo.com/busca/?q=ppp&order=recent&page=1&from=now-1w")

#correção da url duplicada
#print(url.replace('g1.globo.com//','',1 ))
#url = url.replace('g1.globo.com//','',1 )
#print(url)

#request
page = requests.get(url)

print(page.status_code)

if page.status_code == 200:

    soup = BeautifulSoup(page.text, features="html.parser")
    for noticia in soup.select("div.widget--info__text-container"):
        print(noticia.text)