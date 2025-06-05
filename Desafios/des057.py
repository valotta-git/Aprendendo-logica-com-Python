n = int (input ('Digite um número para calcular o fatorial: '))
c = n
m = 1
while c > 0:
    print ('{}'.format (c), end='')
    print (' x ' if c > 1 else ' = ', end='')
    m *= c
    c -= 1
print (m)
'''n = int (input ('Digite um número para calcular o fatorial: '))
m = 1
for n in range (n,0,-1):
    print (n,end='')
    print (' x ' if n > 1 else ' = ', end='')
    m *= n
print (m)'''
