maior = 0
menor = 0
for c in range (1,6):
    peso = int (input ('Qual o peso da {}º pessoa? '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print ('O maior peso lido foi de {}Kg'.format (maior))
print ('O menor peso lido foi de {}Kg'.format (menor))