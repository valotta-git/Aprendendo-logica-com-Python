val = []
'''for c in range (0,5):
    n = int (input ('Digite um valor: '))
    if c == 0:
        val.append(n)
        print ('Valor adicionado ao final da lista')
    if c == 1:
        if n < val [0]:
            val.insert(0,n)
            print ('Valor adicionado a posição 0 da lista')
        if n > val [0]:
            val.append(n)
            print ('Valor adicionado ao final da lista')
    if c == 2:
        if n < val [0] and n < val [1]:
            val.insert(0,n)
            print ('Valor adicionado a posição 0 da lista')
        if n > val [0] and n > val[1]:
            val.append(n)
            print ('Valor adicionado ao final da lista')
        if n > val [0] and n < val[1]:
            n = val [1]
            print ('Valor adicionado a posição 1 da lista')
    if c == 3:
        if n < val [0] and n < val [1] and n < val [2]:
            val.insert(0,n)
            print ('Valor adicionado a posição 0 da lista')
        if n > val [0] and n > val[1] and n > val [2]:
            val.append(n)
            print ('Valor adicionado ao final da lista')
        if n > val [0] and n < val[1]:
            n = val [1]
            print ('Valor adicionado a posição 1 da lista')
        if n > val [1] and n < val[2]:
            n = val [2]
            print ('Valor adicionado a posição 2 da lista')
    if c == 4:
        if n < val [0] and n < val [1] and n < val [2] and n < val [3]:
            val.insert(0,n)
            print ('Valor adicionado a posição 0 da lista')
        if n > val [0] and n > val[1] and n > val [2] and n > val [3]:
            val.append(n)
            print ('Valor adicionado ao final da lista')
        if n > val [0] and n < val[1]:
            n = val [1]
            print ('Valor adicionado a posição 1 da lista')
        if n > val [1] and n < val[2]:
            n = val [2]
            print ('Valor adicionado a posição 2 da lista')
        if n > val [2] and n < val[3]:
            n = val [3]
            print ('Valor adicionado a posição 3 da lista')
print (val)'''
# for c in range(0,5):
#     n = int (input ('Digite um número: '))
#     if c == 0 or n > val[-1]:
#         val.append(n)
#         print ('Valor adicionado ao final da lista')
#     else: