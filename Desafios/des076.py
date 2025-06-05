val = []
while True:
    n = int (input ('Digite um valor: '))
    if n in val:
        print ('Valor duplicado. não adicionado')
    else:
        val.append(n)
        print ('Valor adicionado!')
    r = str (input ('Quer continuar ? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
val.sort()
print (f'Você digitou os valores {val}')