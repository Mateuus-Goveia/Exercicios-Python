"""Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K / 3,6 sendo K a velocidade em
km/h e M em m/s."""

K = float(input('Digite a velocidade em km/h: '))
M = K / 3.6
print('{:.2f}km/h é o mesmo que {:.2f}m/s'.format(K, M))
print('FIM')
