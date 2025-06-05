from random import choice
num = int (input ('qual número o computador pensou? '))
lista = [1,2,3,4,5]
escolha = choice(lista)
print ('O computador escolheu o número {}'.format(escolha))
if num == escolha:
    print ('Parabéns você acertou!')
else:
    print ('Tente novamente')

'''from random import randint
from time import sleep

pc = randint (0,5)
print ('-=-'* 20)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('-=-'* 20)
sleep(1)
jogador = int (input ('Em que número eu pensei? '))
print ('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print ('Parabéns!! Você venceu')
else:
    print ('Resposta errada, pensei no {} e não no {}'.format (pc, jogador))'''