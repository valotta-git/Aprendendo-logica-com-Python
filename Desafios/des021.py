nome = str (input ('Digite o seu nome completo: ')).title().strip()
div = nome.split()
print ('O seu primeiro nome é: {}'.format (div [0]))
print ('O seu último nome é: {}'.format (nome[len (nome)-1]))
# o "len -1" pega a ultima separação de um split -2 pega a penultima e assim por diante