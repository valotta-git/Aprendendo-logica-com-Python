soma = cont = 0
while True:
    n = int (input ('Digite um valor (999 par para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print (f'Você digitou {cont} valores e a soma deu {soma}')