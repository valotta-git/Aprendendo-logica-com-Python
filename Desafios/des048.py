t1 = int (input ('Primeiro termo: '))
razao = int (input ('Razão: '))
décimo = t1 + (10 - 1) * razao # fórmula para termos
for c in range (t1,décimo + razao, razao,):
    print ('{} -> '.format (c), end = '')
print ('FIM')