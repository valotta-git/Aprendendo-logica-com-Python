print ('-='*20)
print ('Somador de números! Para parar digite 999')
print ('-='*20)
#n = 0
#cont = 0
#soma = 0
n = cont = soma = 0
n = int (input ('Digite um número: '))
while n != 999:
    cont += 1
    soma += n
    n = int (input ('Digite um número: '))
print ('Fim! Você digitou {} números e a soma deles é = {}'.format (cont, soma))