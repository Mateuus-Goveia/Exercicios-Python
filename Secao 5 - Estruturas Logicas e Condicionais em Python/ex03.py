num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** (1/2)
    print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
else:
    quadrado = num ** 2
    print('O numero {} ao quadrado é igual a {}'.format(num, quadrado))
print('FIM')
