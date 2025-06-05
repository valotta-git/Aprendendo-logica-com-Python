from datetime import date
nas = int (input ('Em que ano você nasceu? '))
ano = date.today().year
if nas > (ano - 18):
    print ('Você ainda não precisa se alistar, ainda falta(m) {} ano(s)'.format ((nas + 18)- ano))
elif nas < (ano - 18):
    print ('Você ja deveria ter se alistado {} ano(s) atrás'.format((ano - 18)- nas))
else:
    print ('\33[32mVocê deve se alistar esse ano!\33[m')