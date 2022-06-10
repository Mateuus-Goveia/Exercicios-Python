"""Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = C + 273,15 sendo C a temperatura em Celsius e K a
temperatura em Kelvin."""

print('Conversor Celsius para Kelvin')
C = float(input('Digite em ºC: '))
K = C + 273.15
print('{}ºC é o mesmo que {}\033[;1mK'.format(C, K))
print('FIM')
