print ('='*30)
print ('{:^30}'.format ('BANCO V'))
print ('='*30)
valor = 0
while True:
    valor = int (input ('Qual valor você quer sacar? R$ '))
    if valor > 0:
        r50 = valor // 50
        if valor >= 50:
            print (f'{r50} notas de 50 sacadas ')
        sobra = valor % 50
        if sobra == 0:
            break
        elif sobra > 0:
            sobra == valor
        if sobra >= 20:
            r20 = sobra // 20
            print (f'{r20} notas de 20 sacadas ')
            sobra = valor % 20
            if sobra == 0:
                break
        if sobra >= 10:
            r10 = sobra // 10
            print (f'{r10} notas de 10 sacadas ')
            sobra = valor % 10
            if sobra == 0:
                break
        if sobra >= 1:
            r1 = sobra // 1
            print (f'{r1} notas de 1 sacadas ')
            sobra = valor % 1
            if sobra == 0:
                break
'''tt = 1209 // 50
print (tt)
print (1209 % 50)'''