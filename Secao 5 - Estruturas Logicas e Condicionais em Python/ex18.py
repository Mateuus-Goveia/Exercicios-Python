"""Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo."""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número: '))
print('Calculadora básica digite:')
print('[1] Para somar')
print('[2] Para subtrair')
print('[3] Para multiplicar')
print('[4] Para dividir')
Ope = int(input('Digite aqui: '))
if Ope == 1:
    print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}')
elif Ope == 2:
    print(f'A subtração entre {num1} e {num2} é igual a {num1 - num2}')
elif Ope == 3:
    print(f'A multiplicação entre {num1} e {num2} é igual a {num1 * num2}')
elif Ope == 4:
    print(f'A divisão entre {num1} e {num2} é igual a {num1 / num2}')
else:
    print('Número inválido')
print('FIM')
