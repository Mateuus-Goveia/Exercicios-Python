"""Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:"""

num = int(input('Digite um numero: '))
if num > 0:
    raiz = num ** (1/2)
    quadrado = num ** 2
    print(f'{num} ao quadrado é o mesmo que {quadrado}')
    print(f'A raiz de {num} é igual a {raiz:.2f}')
print('FIM')
