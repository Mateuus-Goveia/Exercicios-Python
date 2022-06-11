"""Faça um programa para ler as dimensões de um terreno (comprimento "c" e largura "l"),
bem como o preço do metro de tela "p". Imprima o custo para cercar este mesmo terreno
com tela."""

print('Descubra o valor para cercar todo terreno.')
C = float(input('Digite o comprimento do terreno: '))
L = float(input('Digite a largura do terreno: '))
D = C + L
P = float(input('Digite o valor do metro da tela R$ '))
print(f'Para cercar todo terreno de tela vai precisar de R${D * P:.2f}')
print('FIM')
