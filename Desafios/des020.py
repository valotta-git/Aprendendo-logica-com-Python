fr = str (input ('Digite uma frase: ')).lower()
print ('a frase tem {} letras "a"'.format (fr.count('a')))
print ('aparece na posição {} pela primeira vez'.format (fr.find('a')+1))#+1 pra não começar contando do 0
print ('e na {} pela ultima'.format (fr.rfind('a')+1))