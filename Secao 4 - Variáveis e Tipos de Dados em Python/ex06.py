"""Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é F = C * (9,0 / 5:0) + 32,0 sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius."""

print('=' * 36)
print('Conversor de Celsius para Fahrenheit')
print('=' * 36)
C = float(input('Digite quantos Cª: '))
F = C * (9.0/5.0) + 32
print('{}ªC é o mesmo que {}F'.format(C, F))
print('FIM')
