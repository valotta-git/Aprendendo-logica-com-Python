while True:
    n = int (input ('Você quer ver a  tabuada de qual valor? '))
    print ('-'*40)
    if n < 0:
        break
    for c in range (1, 11):
        print (f'{n} x {c} = {n*c}')
    print ('-'*40)
print ('Programa encerrado')