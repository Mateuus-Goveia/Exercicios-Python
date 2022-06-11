"""Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste número."""

from math import log

num = int(input('Digite um numero positivo: '))
if num < 0:
    print('Numero invalido.')
else:
    log = log(num)
    print(f'Logaritmo de {num} é igual a {log:.2f}')
print('FIM')
