frase =  ('Curso em vídeo python') #20 caracteres o 0 e espaços contam
print ((frase[9],frase[9:13],frase[9:21],frase[9:21:2],frase[:5],frase[15:],frase[9::3]))
print ((len(frase),frase.count('o'),frase.count('o',0,13),frase.find('deo'),frase.find('uno'),'Curso' in frase))
print ((frase.replace('python','android'),frase.upper(),frase.lower(),frase.capitalize(),frase.title(),frase.split()))    
print (('-'.join(frase))) #pode ser espaço  

'''
O ultimo caractere citado não conta, no comando count não precisa de ":", no código frase.count('o',0,13) ele pede
quantos o's tem do 0 ao 13, "find" fala aonde o que você procura começou,
'''
frases = ('   Aprenda python  ')
print ((frases.strip(),frases.rstrip(),frases.lstrip()))