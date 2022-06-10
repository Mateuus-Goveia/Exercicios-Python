"""Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5,0 * (F - 32,0) / 9,0 sendo C a temperatura em Celsius
 e F a temperatura em Fahrenheit."""

print('=' * 36)
print('Conversor de Fahrenheit para Celsius')
print('=' * 36)
F = float(input('Digite em °F: '))
C = 5.0 * (F - 32.0) / 9.0
print('{}ºF é o mesmo que {:.4f}'.format(F, C))
print('FIM')
