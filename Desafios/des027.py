'''ano = int (input ('Digite um ano: '))
bisx = ano % 4
if bisx == 0:
    print ('O ano que você digitou é bissexto!')
else:
    print ('O ano que você digitou não é bissexto!')'''
from datetime import date #data atual do SO
ano = int (input ('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # código especifico pra ano bissexto
    print ('O ano {} é bissexto'.format (ano))
else:
    print ('o ano {} não é bissexto'.format (ano))