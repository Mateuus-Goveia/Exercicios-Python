"""Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem "Números iguais" """

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('{} é maior que o número {} !!'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que o  número {} !!'.format(num2, num1))
else:
    print('Números iguais')
print('FIM')
