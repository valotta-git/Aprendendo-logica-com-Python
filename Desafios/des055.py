from random import randint
pc = randint (0, 10)
ok = False
tent = 0
while not ok:
    jogador = int (input ('Qual o seu palpite? '))
    tent += 1
    if jogador == pc:
        ok = True
    else:
        if jogador < pc:
            print ('Mais... tente de novo')
        elif jogador > pc:
            print ('Menos... tente de novo')
print ('Acertou com {} tentativas!'.format(tent))
