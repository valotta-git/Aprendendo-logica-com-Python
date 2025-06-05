n = int (input ('Digite um número em 0 e 20 que quer ler por extenso: '))
num = ('ZERO','UM','DOIS','TRÊS','QUARTO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
       'ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE',
                    'DEZOITO','DEZENOVE','VINTE')
while n > 20 or n < 0:
    n = int (input ('O número deve estar entre 0 e 20. Digite novamente: '))
print (f'Você digitou o número {num[n]}')