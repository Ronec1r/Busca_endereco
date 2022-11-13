import requests
from bs4 import BeautifulSoup

#input de dados
link='http://cep.la/'
info=input('Insira seu CEP: ')

#request do link especifico
link=link+info
r=requests.get(link)
html=r.text

sopa=BeautifulSoup(html,'html.parser')

#amostra dos dados buscado
print("----------------")
if(sopa.find_all('div',id='cep')):
    print("Seu endereço é: ")
    for i in sopa.find_all('div',id='cep'): 
        print(i.text)
else:
    print("Cep não encontrado")
print("----------------")
