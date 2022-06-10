"""Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
 em vista que o desconto foi de 12%"""

P = float(input('Digite o valor do produto R$'))
D = P - (P / 100 * 12)
print('Seu produto com 12% de desconto vai sair a \033[1;32m{}'.format(D))
print('FIM')
