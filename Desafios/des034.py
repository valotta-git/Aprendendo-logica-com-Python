num1 = int (input ('Digite um número inteiro: '))
num2 = int (input ('Digite mais um número inteiro: '))
if num1 > num2:
    print ('\033[4;32mO primeiro número é maior\33[m')
elif num2 > num1:
    print ('\33[4;33mO segundo número é maior\33[m')
else:
    print ('os números contém valores iguais')