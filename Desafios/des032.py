casa = float (input ('Qual o valor da casa? R$'))
sal = float (input ('Qual o seu salário? R$'))
anos = int (input ('Em quantos anos você quer pagar a casa? '))
mensal = casa / (anos * 12)
print ('\33[1;33mPara pegar uma casa de R${:.2f} em {} anos.'.format(casa, anos), end=' ')
print ('A prestação será de R$ {:.2f}\33[m'.format(mensal))
if sal * 0.3 < mensal:
    print ('\033[31mEmpréstimo reprovado :(\033[m')
else:
    print ('\033[32mEmpréstimo aprovado!!\033[m')