num = float(input('Digite um número positivo: '))
if num > 0:
    raiz = num ** (1/2)
    print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
else:
    print('Seu número não é valido -.-')
print('FIM')
