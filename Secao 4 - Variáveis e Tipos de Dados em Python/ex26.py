"""Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0,0001 sendo M a área em metros quadrados e H
a área em hectares."""

M = float(input('Digite quantos m²: '))
H = M * 0.0001
print('{}m² é o mesmo que {} hectares.'.format(M, H))
print('FIM')
