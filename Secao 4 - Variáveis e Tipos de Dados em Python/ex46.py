"""Faça um programa que leia um número inteiro positivo de trÊs dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

                        NúmeroLido = 123
                       NúmeroGerado = 321"""

num = int(input('Digite um numero de (100 a 999): '))
num = str(num)
print('{} de trás para frente é {}'.format(num, num[::-1]))
print('FIM')
