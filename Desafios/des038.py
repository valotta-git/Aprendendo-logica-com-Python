print ('-='*20)
print ('Analisador de triangulos')
print ('-='*20)
s1 = float (input ('primeiro segmento: '))
s2 = float (input ('segundo segmento: '))
s3 = float (input ('terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print ('Os segmentos acima podem formar um triangulo, esse triangulo é ', end = '')
    if s1 == s2 == s3:
        print ('Equilatero')
    elif s1 != s2 != s3 !=s1:
        print ('Escaleno')
    else:
        print ('Isóceles')
else:
    print ('os segmentos acima não podem formar um triangulo')