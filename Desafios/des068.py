lanche = 'Hamburguer', 'Suco', 'pera', 'Mamão', 'Batata frita'

for comida in lanche:
    print (f'Eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, com in enumerate (lanche):
    print (f'Eu vou comer {com} na posição {pos}')