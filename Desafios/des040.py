preco = float (input ('Preço das compras: R$ '))
print ('Formas de pagamento \n[ 1 ] À vista dinheiro/pix\n[ 2 ] À vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pag = int (input ('Qual a forma de pagamento? '))
if pag == 1:
    print ('\033[32mPagamento no dinheiro ou pix 10% de desconto fica o valor de R${}\033[m'.format (preco - (preco / 10)))
elif pag == 2:
    print ('\033[32mPagamento no cartão a vista com 5% de desconto fica o valor de {}R$\33[m'.format (preco - (preco / 20)))
elif pag == 3:
    print ('\033[32mPagamento em 2x no cartão fica o valor de R${}\33[m'.format (preco))
elif pag == 4:
    print ('\033[32mPagamento em 3x ou mais no cartão com 20% de juros fica com o valor de {}\033[m'.format(preco + (preco * 0.2)))
else:
    print ('não temos essa forma de pagamento por favor tente outro jeito')