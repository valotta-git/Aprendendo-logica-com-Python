km = float (input ('Quantos km tem sua viagem? '))
'''if km <= 200:
    custo = 0.50*km
    print ('Sua viagem vai custar R$ {:.2f} reais'.format(custo))
else:
    custo2 = 0.45*km
    print ('Sua viagem vai custar R$ {:.2f} reais'.format(custo2))'''
preço = km * 0.50 if km <= 200 else km * 0.45
print ('O preço da sua passagem será de R${:.2f}'.format (preço))