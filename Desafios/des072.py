val = (int (input ('Digite um valor: ')),
       int (input ('Digite mais um: ')),
       int (input ('Mais uma vez: ')),
       int (input ('O último: ')))
print (f'O valor 9 apareceu {val.count(9)} vezes')
if 3 in val:   
    print (f'O 3 aparece primeiro na posição {val.index(3)+1}')
else:
    print ('O valor 3 não foi digitado')
for v in val:
    if v % 2 == 0:
        print (f'o valores pares digitados foram: {v}',end=' ')