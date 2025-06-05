vel = int (input ('Qual é a velocidade do seu carro? '))
if vel > 80:
    print ('Você foi multado em R$ {} reais '.format ((vel-80)*7))
else:
    print ('Parabéns sua viagem não teve multas por velocidadade alta!')
