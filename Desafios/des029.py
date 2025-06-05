salary = float (input ('Qual o seu salário? '))
if salary <= 1250:
    #aumento = salary * 0.15
    print (salary + salary * 0.15)
    print ('O seu salario teve um aumento de R${:.2f} reais'.format (salary * 0.15))
else:
    print (salary + salary * 0.1)
    print ('O seu salario teve um aumento de R${} reais'.format (salary * 0.1))