"""Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos."""

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
if num1 > num2:
    dif = num1 - num2
    print(f'{num1} É maior que {num2} com a diferença de {dif} números!!')
elif num2 > num1:
    dif = num2 - num1
    print(f'{num2} É maior que {num1} com a diferença de {dif} números!!')
else:
    print('Os números são iguais tente novamente')
print('FIM')
