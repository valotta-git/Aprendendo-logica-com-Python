from random import randint
vit = 0
while True:
    p = int (input ('JOGUE um número: '))
    pc = randint (1,10)
    tot = pc + p
    tipo = ' '
    while tipo not in ('IP'):
        tipo = str (input ('Quer impar ou par [I/P]? ')).strip().upper()[0]
    if tot % 2 == 0:
        if tipo == 'P':
            print (f'\033[32mVocê venceu!!\033[m O computador jogou {pc} e você jogou {p} e deu Par')
            vit += 1
        if tipo == 'I':
            tipopc = 'Par'
            break
    if tot % 2 == 1:
        if tipo == 'I':
            print (f'\033[32mVocê venceu!!\033[m O computador jogou {pc} e você jogou {p} e deu Impar')
            vit += 1
        if tipo == 'P':
            tipopc = 'Impar'
            break
print (f'\033[31mGAME OVER!\033[m O computador jogou {pc} e você jogou {p} que deu {tipopc}. Você venceu {vit} vezes')