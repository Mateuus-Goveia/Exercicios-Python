"""Faça um programa que leia um número inteiro e verifique se este número é par ou
ímpar."""

num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} É UM NUMERO PAR !!!')
elif num % 2 == 1:
    print(f'{num} É UM NUMERO ÍMPAR !!!')
print('FIM')
