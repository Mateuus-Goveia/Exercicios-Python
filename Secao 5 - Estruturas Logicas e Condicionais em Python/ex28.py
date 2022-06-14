"""Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica (x * y * z) / (1 / 3)
(b) Ponderada: (x + 2 * y + 3 * z) / 6
(c) Harmônica: 1 / (1 / x + 1 / y + 1 / z)
(d) Aritmética: (x + y + z) / 3"""

print('Calculadora de médias')
x = int(input('Digite x: '))
y = int(input('Digite y: '))
z = int(input('Digite z: '))
if x >= 0 and y >= 0 and z >= 0:
    print('[1] Geométrica')
    print('[2] Ponderada')
    print('[3] Harmônica')
    print('[4] Aritmética')
    M = int(input('Digite aqui: '))
    if M == 1:
        R = x ** (1/3) * y ** (1/3) * z ** (1/3)
        print(f'Media Geométrica {R:.2f}')
    elif M == 2:
        R = (x + 2 * y + 3 * z) / 6
        print(f'Media Ponderada {R:.2f}')
    elif M == 3:
        R = 1 / (1 / x + 1 / y + 1 / z)
        print(f'Media Harmônica {R:.2f}')
    elif M == 4:
        R = (x + y + z) / 3
        print(f'Media Aritmética {R:.2f}')
    else:
        print('Opção inválida')
else:
    print('Valor invalido digite um número inteiro e positivo.')
print('FIM')
