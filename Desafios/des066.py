tot = pmil = menor = conta = 0
barato = ' '
while True:
    produto = str (input ('Nome do produto: ')).strip()
    preco = int (input ('Preço: '))
    tot += preco
    if preco > 1000:
        pmil += 1
    conta += 1
    if conta == 1 or menor > preco:
        menor = preco
        barato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str (input ('Quer continuar: [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print (f'O total da compra deu R$ {tot:.2f}')
print (f'Temos {pmil} produto(s) acima de R$ 1000.00')
print (f'O produto mais barato foi o {barato} custando {menor:.2f}')