"""Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3,6 sendo K a velocidade
em km/h e M em m/s"""

M = float(input('Distancia em m/s: '))
K = M * 3.6
print('{:.2f}m/s é o mesmo {:.2f}'.format(M, K))
print('FIM')
