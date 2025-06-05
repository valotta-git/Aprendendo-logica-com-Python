for c in range (0,5,2):
    print (c)

i = int (input ('Inicio: '))
f = int (input ('Fim: '))
p = int (input ('Passo: '))
for c in range (i, f+1, p):
    print (c)
print ('FIM')
val = 0
s = 0
for c in range (0,4):
    n = int (input ('Digite um valor: '))
    val = val + 1
    s += n
print ('O somatório de todos os {} valores foi {}'.format (val,s))