cdd = str (input ('Digite o nome de uma cidade: ')).strip()
#print (cdd[:5].upper() == 'SANTO')
div = cdd.split()
print ('A cidade começa com "Santo"?')
print (div[0].upper() == 'SANTO')
#o primeiro código retorna true até o quinto caractere ou seja, santos ou santooooosnns retorna true da mesma forma