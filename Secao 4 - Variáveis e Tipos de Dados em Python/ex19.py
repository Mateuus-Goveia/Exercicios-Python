"""Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = L / 1000 sendo L o volume em litros e M o volume em metros
cúbicos."""

L = float(input('Quantidade de litros: '))
M = L / 1000
print('{} litros é o mesmo que {}m³'.format(L, M))
print('FIM')
