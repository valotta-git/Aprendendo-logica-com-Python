v = input('Digite algo: ')
print ('\33[1;31;47mO tipo primitivo desse valor é\33[m',type(v))
print ('\33[4;32;47mSó tem espaços?\33[m',v.isspace())
print ('\33[7mÉ um número?\33[m',v.isnumeric())
print ('\33[4;33;47mÉ alfabético?\33[m',v.isalpha())
print ('\33[36;47mÉ alfanumérico?\33[m',v.isalnum())
print ('\33[34;47mEstá em maiúsculas?\33[m',v.isupper())
print ('\33[35;47mEstá em minúsculas?\33[m',v.islower())
print ('\33[37;46mEstá capitalizada?\33[m',v.istitle()) #começa com maiuscula e o resto é miúscula