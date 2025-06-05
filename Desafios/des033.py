num = int (input ('Digite um número interiro: '))
print ('''Escolha uma das bases para a conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL 
[ 3 ] Converter para HAXADECIMAL''') # ''' no print pode ser usado desa forma para quebrar a linha
opção = int (input ('Sua opção: '))
if opção == 1:
    print ('{} Convertido para binário é igual a {}'.format (num, bin(num)[2:]))
elif opção == 2:
    print ('{} Convertido para octal é igual a {}'.format (num, oct(num)[2:])) #2: no código quer dizer para pegar o resultado a partir do terceiro digito
elif opção == 3:
    print ('{} Convertido para hexadecimal é igual a {}'.format (num, hex(num)[2:]))
else:
    print ('\33[7;33mOpção inválida: Tente novamente.\33[m')