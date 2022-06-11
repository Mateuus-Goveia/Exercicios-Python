"""Faça um programa que receba dois números e mostre qual deles é o maior"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print(f'{num1} é maior que o número {num2} !!')
elif num2 > num1:
    print(f'{num2} é maior que o  número {num1} !!')
else:
    print('Os números são iguais tente novamente..')
print('FIM')
