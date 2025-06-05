math = n = cont = soma = maior = menor = 0
while math != 2:
    n = int (input ('Digite um número: '))
    math = int (input ('Quer continuar? [1] SIM [2] NÃO : '))
    while math != 1 and math != 2:
        math = int (input ('Resposta inválida, Quer continuar? [1] SIM [2] NÃO : '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print ('FIM! Você digitou {} números, a média entre eles é {:.2f}, o menor é o {} e o maior é o {}'.format (cont, media, menor, maior))