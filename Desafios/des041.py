from random import randint
print ('-='*20)
print ('vamos jogar jokenpô')
print ('=-'*20)
choice = str (input ('Escolha pedra, papel ou tesoura: ')).upper()
jogo = ['PAPEL','PEDRA','TESOURA']
ale = randint(0,2)
mist = jogo[ale]
print ('O computador jogou {}'.format (mist))
print ('Você jogou {}'.format (choice))
if mist == 'PEDRA':
    if choice == 'PEDRA':
        print ('EMPATE')
    elif choice == 'PAPEL':
        print ('VOCÊ GANHOU')
    elif choice == 'TESOURA':
        print ('VOCÊ PERDEU')
    else:
        print ('\033[31mJogada inválida\033[m')
elif mist == 'PAPEL':
    if choice == 'PEDRA':
        print ('VOCÊ PERDEU')
    elif choice == 'PAPEL':
        print ('EMPATE')
    elif choice == 'TESOURA':
        print ('VOCÊ GANHOU')
    else:
        print ('\033[31mJogada inválida\033[m')

elif mist == 'TESOURA':
    if choice == 'PEDRA':
        print ('VOCÊ GANHOU')
    elif choice == 'PAPEL':
        print ('VOCÊ PERDEU')
    elif choice == 'TESOURA':
        print ('EMPATE')
    else:
        print ('\033[31mJogada inválida\033[m')