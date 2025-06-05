'''

sequencia de comandos stilo ; cor ; fundo
/estilo/
0 none
1 bold
4 underline
7 negative
/cor/
30 == branco
31 == vermelho
32 == verde
33 == amarelo
34 == azul
35 == roxo
36 == ciano
37 == cinza
/fundo/
mesma sequencia de cor com 40,41,42...

'''
t1 = 't1'
t2 = 't2'
t3 = 't3'
t4 = 't4'
t5 = 't5'
t6 = 't6'
print ('testes\033[30;41m{}\033[4;33;44m{}\33[1;35;43m{}\33[30;42m{}\33[m{}\33[7;36m{}\033[m'.format(t1,t2,t3,t4,t5,t6))