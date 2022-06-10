"""Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61 * M sendo K a distância em quilômetros e M em milhas."""

print('Conversor milhas para quilômetros')
M = float(input('Digite distancia em milhas: '))
K = 1.609344 * M
print('{} milhas é o mesmo que {}km'.format(M, K))
print('FIM')
