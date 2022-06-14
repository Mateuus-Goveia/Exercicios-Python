"""Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde "h" corresponde a altura):
● Homens: (72,7 * h) - 58
● Mulheres: (62,1 * h) - 44,7"""

A = float(input('Digite a altura: '))
print('Digite o sexo')
print('[1] para masculino')
print('[2] para feminino')
S = float(input('Digite aqui: '))
if S == 1:
    IMC = (72.7 * A) - 58
    print(f'Seu peso ideal é {IMC:.2f}')
elif S == 2:
    IMC = (62.1 * A) - 44.7
    print(f'Seu peso ideal é {IMC:.2f}')
else:
    print('Valor do sexo invalido tente novamente.')
print('FIM')
