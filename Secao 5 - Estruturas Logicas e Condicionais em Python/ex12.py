from math import log

num = int(input('Digite um numero positivo: '))
if num < 0:
    print('Numero invalido.')
else:
    log = log(num)
    print('Logaritimo de {} é igual a {:.2f}'.format(num, log))
print('FIM')
