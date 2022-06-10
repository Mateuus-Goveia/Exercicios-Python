"""Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A
fórmula de conversão é: M = A * 4048,58 sendo M a área em metros quadrados e A a
área em acres."""

A = float(input('Digite o valor em acres: '))
M = A * 4048.58
print('{} acres é o mesmo que {}m²'.format(A, M))
print('FIM')
