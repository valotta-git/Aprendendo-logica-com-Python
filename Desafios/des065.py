tot18 = toth = totmut = 0
while True:
    print ('-'*30)
    print ('Cadastre uma pessoa')
    print ('-'*30)
    id = int (input ('IDADE: '))
    sexo = str (input ('SEXO: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str (input ('SEXO: ')).strip().upper()[0]
    if id >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and id < 20:
        totmut += 1
    cont = ' '
    while cont not in 'SN':
        cont = str (input ('Quer continuar [s/n]? ')).strip().upper()[0]
    if cont == 'N':
        break
print (f'Total de pessoas com mais de 18 anos: {tot18}\nAo todo temos {toth} homens cadastrados\nE temos {totmut} mulheres com menos de 20 anos')
