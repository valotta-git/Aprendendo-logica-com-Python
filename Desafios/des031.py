nome = str (input ('Qual o seu nome? ')).strip().title()
if nome == 'Victor':
    print ('WOOOOOOOW que nome bonito!!')
elif nome == 'Thais':
    print ('Olá Thais')
elif nome == 'Isadora':
    print ('Olá Isadora, que nome bonito')
elif nome == 'Solange' or nome == 'Maria' or nome == 'Rosana':
    print ('Nomes antigos... interessante')
else:
    print ('Seu nome é bem normal')
print ('Tenha um bom dia {}!'.format (nome))