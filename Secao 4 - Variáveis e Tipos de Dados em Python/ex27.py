"""Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000 sendo M a área em metros quadrados e H
a área em hectares."""

H = float(input('Digite quantos hectares: '))
M = H * 10000
print('{} hectares é o mesmo que {}m²'.format(H, M))
print('FIM')
