print ('Grador de PA')
print ('-='*10)
primeiro = int (input ('Digite o primeiro termo: '))
razão = int (input ('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print ('{} -> '.format(termo),end='')
        termo += razão
        cont += 1
    print ('Pausa')
    mais = int (input ('Quantos termos a mais você quer? '))
print ('Progressão finalizada com {} termos mostrados!'.format (cont))