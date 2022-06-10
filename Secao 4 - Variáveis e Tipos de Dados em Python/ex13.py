"""Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = K / 1,61 sendo K a distância em quilômetros e M em milhas."""

print('Conversor quilômetros para milhas.')
km = float(input('Distancia em km: '))
milhas = km / 1.609344
print('{}km é o mesmo que {:.7f} milhas'.format(km, milhas))
print('FIM')
