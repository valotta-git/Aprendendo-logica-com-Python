s = str (input ('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
while s not in 'MF':
    s = str (input ('Sexo inválido, digite novamente: ')).strip().upper()[0]
print ('Sexo {} registrado com sucesso '.format (s))
    