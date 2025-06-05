nome = str (input ('Digite o seu nome completo: ')).strip() 
#a função strip pode ser chamada se identificar antes que é uma string
print ('Analisando o seu nome...')
print ('seu nome em letras minúsculas é: {}'.format (nome.lower()))
print ('seu nome em letras maiúsculas é: {}'.format (nome.upper()))
print ('seu nome tem ao todo {} letras'.format (len(nome) - nome.count(' '))) #quantos caracteres tem menos os espaços
div = nome.split()
print ('seu primeiro nome é {} e tem {} letras'.format(div[0], len(div[0])))