num = int (input ('Digite um número: '))
num1 = int (input ('Digite outro: '))
num2 = int (input ('Digite mais um: '))

menor = num
if num1<num and num1<num2:
    menor = num1
if num2<num1 and num2<num:
    menor = num2
maior = num1
if num>num1 and num>num2:
    maior = num
if num2>num1 and num2>num:
    maior = num2
print ('O maior número é o {} e o menor é {}'.format (maior, menor))