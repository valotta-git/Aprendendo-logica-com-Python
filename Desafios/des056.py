from time import sleep
n1 = int (input ('Digite o primeiro valor: '))
n2 = int (input ('Digite o segundo valor: '))
print ('O que você quer fazer com esses valores?')
math = 0
while math != 5:
    print ('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair\n''')
    math = int (input ('Qual a sua opção: '))
    if math == 1:
        print ('{} + {} = {}'.format (n1, n2, n1 + n2))
    elif math == 2:
        print ('{} x {} = {}'.format (n1, n2, n1 * n2))
    elif math == 3:
        if n1 > n2:
            print ('O maior número é o {}'.format (n1))
        else:
            print ('O maior número é o {}'.format (n2))
    elif math == 4:
        n1 = int (input ('Digite o primeiro valor: '))
        n2 = int (input ('Digite o segundo valor: '))
    elif math == 5:
        print ('Finalizando...')
    else:
        print ('Opção inválida tente de novo...')
        n1 = int (input ('Digite o primeiro valor: '))
        n2 = int (input ('Digite o segundo valor: '))
    sleep (1)
print ('O programa foi finalizado!')