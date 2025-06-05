idade = 0
velho = 0
idhvelho = 0
nomehvelho = ''
mulheru20 = 0
for c in range(1,5):
    print ('--- {}º pessoa ----'.format(c))
    n = str (input ('Nome: ')).strip()
    i = int (input ('Idade: '))
    s = str (input ('sexo [M/F]: ')).strip()
    idade += i
    if c == 1 and s in 'Mm':
        idhvelho = i
        nomehvelho = n
    if s in 'Mm' and i > idhvelho:
        idhvelho = i
        nomehvelho = n
    if s in 'Ff' and i < 20:
        mulheru20 += 1

print ('A média de idade do grupo é de {} anos!'.format(idade/4))
print ('O homem mais velho tem {} anos e se chama {}.'.format (idhvelho,nomehvelho))
print ('E ao todo são {} mulheres com menos de 20 anos'.format (mulheru20))