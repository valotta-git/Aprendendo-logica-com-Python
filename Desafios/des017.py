'''
num = int (input ('Digite um número de 0 a 9999: '))
n = str(num)
print ('O seu número tem\n{} Unidade\n{} dezena\n{} centena\n{} milhar'.format (n[0], n[1], n[2], n[3]))
#nesse jeito o código só roda se tiver todos os números das casas citados

'''
num = int (input ('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('unidade: {}'.format (u))
print ('dezena: {}'.format (d))
print ('centena: {}'.format (c))
print ('milhar: {}'.format (m))

#explicação aula ex23 minuto 6