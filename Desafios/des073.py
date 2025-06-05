print ('-'*50)
print ('{:^50}'.format ('LISTAGEM DE PREÇOS'))
print ('-'*50)
prod = ('Lapis', 5.50,
'Caderno', 10,
'notebook', 2490,
'estojo', 25.90,
'compasso', 30,
'caderno', 50)
for org in range (len (prod)):
    if org % 2 == 0:
        print (f'{prod[org]:.<39}',end='')
    else:
        print (f'R$ {prod[org]:^5.2f}')