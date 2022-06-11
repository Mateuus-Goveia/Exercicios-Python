num = int(input('Digite um numero: '))
if num > 0:
    raiz = num ** (1/2)
    quadrado = num ** 2
    print('{} ao quadrado é o mesmo que {}'.format(num, quadrado))
    print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('FIM')
