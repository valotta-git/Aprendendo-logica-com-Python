tup = ('casa', 'casinha', 'senhora', 'ornitorrinco', 'garrafa',
       'emprpesa','amasso', 'asfalto', 'paralelepipedo', 'parede')
for cont in tup:
    print (f'\nA palavra {cont} tem as seguintes vogais: ', end='')
    for vog in cont:
        if vog in 'aeiou':
            print (f'{vog} ',end='')