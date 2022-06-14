"""Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

A = (base maior + base menor) * altura / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero."""

B = float(input('Digite a base maior: '))
b = float(input('Digite a base menor: '))
h = float(input('Digite a altura: '))
if B > 0 and b > 0:
    h = (B + b) * h / 2
    print(f'A área do trapézio é {h}')
else:
    print('Digite um número maior que 0')
print('FIM')
