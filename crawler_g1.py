# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

#url coletada pelo robo
url = str("http://g1.globo.com//g1.globo.com/busca/click?q=parceria+publico+privada&p=5&r=1568182739548&u=https%3A%2F%2Fg1.globo.com%2Fmg%2Ftriangulo-mineiro%2Fnoticia%2F2019%2F09%2F10%2Fconstrucao-de-usina-de-energia-solar-em-uberaba-e-tratada-em-audiencia-publica.ghtml&syn=False&key=8a6b7d75384cd8b809f50b1fd8365644")

#correção da url duplicada
print(url.replace('g1.globo.com//','',1 ))
url = url.replace('g1.globo.com//','',1 )
print(url)

#request
page = requests.get(url)

print(page.status_code)

if page.status_code == 200:

    soup = BeautifulSoup(page.text, features="html.parser")
    for noticia in soup.select("h1.content-head__title"):
        print(noticia.text)
