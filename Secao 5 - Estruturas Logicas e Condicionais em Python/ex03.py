"""Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado."""

num = float(input('Digite um numero: '))
if num > 0:
    raiz = num ** (1/2)
    print(f'A raiz quadrada de {num} é igual a {raiz}')
else:
    quadrado = num ** 2
    print(f'O numero {num} ao quadrado é igual a {quadrado}')
print('FIM')
