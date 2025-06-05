from datetime import date
id = int (input ('Em que ano você nasceu? '))
ano = date.today().year
cat = ano - id
if cat <= 9:
    print ('Você pertence a categoria MIRIM')
elif cat <= 14:
    print ('Você pertence a categoria INFANTIL')
elif cat <= 19:
    print ('Você pertence a categoria JUNIOR')
elif cat <= 25:
    print('Você pertence a categoria SÊNIOR')
else:
    print('Você pertence a categoria MASTER')