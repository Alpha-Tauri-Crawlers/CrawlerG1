# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

#url coletada pelo robo
url = ("https://g1.globo.com/")

#correção da url duplicada

#url = url.replace('g1.globo.com//','',1 )
#print(url)

#request
page = requests.get(url)

print(page.status_code)

if page.status_code == 200:

	soup = BeautifulSoup(page.text, features="html.parser")
	for noticia in soup.select("div.bastian-feed-item"):
		print(noticia.text)
