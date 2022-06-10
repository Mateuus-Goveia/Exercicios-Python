"""Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0,91 * J sendo J o comprimento em jardas e M o comprimento
em metros."""

J = float(input('Distancia em Jardas: '))
M = 0.91 * J
print('{} jardas é o mesmo que {}m'.format(J, M))
print('FIM')
