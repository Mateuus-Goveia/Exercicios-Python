"""Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A
fórmula de conversão é: A = M * 0,000247 sendo M a área em metros quadrados e A
a área em acres."""

M = float(input('Digite a área m²: '))
A = M * 0.000247
print('{}m² é o mesmo que {} acres.'.format(M, A))
print('FIM')
