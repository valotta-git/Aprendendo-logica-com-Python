soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma += c #mesma coisa que soma = soma + c
        cont += 1
print ('Os {} valores solicitados somam {}'.format (cont, soma))