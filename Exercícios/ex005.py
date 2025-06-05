dia = int (input ('Quantos dias alugados? '))
km = float (input ('Quantos km rodados? '))
#d1 = km * 0.15
#d2 = dia * 60
preco = (dia * 60) + (km * 0.15)
print ('O total a pagar é de R${:.2f}'.format(preco))