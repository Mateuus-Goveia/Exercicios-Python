"""Escreva um programa que leia as coordenadas "x" e "y" de pontos do "R²" e calcule sua
distância da origem (0,0)."""

x1 = 0
y1 = 0
x2 = int(input('Digite a coordenada x: '))
y2 = int(input('Digite a coordenada y: '))

d1 = (x1-x2) ** 2 + (y1 - y2) ** 2
d2 = d1 ** (1/2)
print('A distância entre os pontos é {:.2f}'.format(d2))
print('FIM')
