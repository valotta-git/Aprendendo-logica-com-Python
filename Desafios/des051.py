from datetime import date
atual = date.today().year
contmai = 0
contmen = 0
for c in range (1,8):
    ano = int (input ('Em que ano a {}º pessoa nasceu?'.format(c)))
    if ano > atual -21:
        idade = 'maior'
        contmai += 1
    else:
        idade = 'menor'
        contmen += 1
print ('Ao todo tivemos {} pessoas maiores de idade \nE também {} pessoas menores de idade'.format (contmai,contmen))
