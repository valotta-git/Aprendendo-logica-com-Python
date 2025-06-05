p = float (input ('Digite o preço do produto: '))
desc = p - p * 0.05
print ('Agora o preço de R${:.2f} está saindo por R${:.2f}'.format(p, desc))