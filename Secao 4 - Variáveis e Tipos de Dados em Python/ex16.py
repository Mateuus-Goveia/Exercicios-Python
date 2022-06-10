"""Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2,54 sendo C o comprimento em centímetros e P o
comprimento em polegadas."""

print('Conversor de Polegadas para centímetros.')
P = float(input('Digite em polegadas: '))
C = P * 2.54
print('{} polegadas é o mesmo que {}cm'.format(P, C))
print('FIM')
