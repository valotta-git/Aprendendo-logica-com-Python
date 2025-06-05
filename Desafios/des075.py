val = []
mai = men = 0
for c in range (0,5):
    val.append(int (input ('Digite um número: ')))
    if c == 0:
        mai = men = val[c]
    else:
        if mai < val[c]:
            mai = val[c]
        if men > val[c]:
            men = val[c]
print (f'Você digitou os valores {val}')
print (f'O maior valor digitado foi o {mai} na ',end='')
for i, c in enumerate (val):
    if c == mai:
        print (f'{i+1}ª posição ', end='')
print (f'\nO menor valor digitado foi o {men} na ',end='')
for i2, c in enumerate (val):
    if c == men:
        print (f'{i2+1}ª posição ', end='')