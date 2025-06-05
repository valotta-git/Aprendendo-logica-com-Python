mat = float (input ('Qual nota o vitinho tirou em matemática? '))
port = float (input ('Qual nota o vitinho tirou em português? '))
media = (mat + port)/2
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print ('Recuperação')
else:
    print ('aprovado')