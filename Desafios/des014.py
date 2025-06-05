from random import choice

al1 = input ('Primeiro aluno: ')
al2 = input ('Segundo aluno: ')
al3 = input ('Terceiro aluno: ')
al4 = input ('Quarto aluno: ')
lista = [al1, al2, al3, al4]
escolha = choice(lista)
print ('o aluno escolhido foi: {}'.format(escolha))

#Esse cóidigo gera qualquer desses nomes aleatóriamente

#al1 = ('joão')
#al2 = ('pedrinho')
#al3 = ('yasmin')
#al4 = ('cassio')
#lista = [al1, al2, al3, al4]
#choice = choice(lista)
#print ('o aluno escolhido foi: {}'.format(choice))