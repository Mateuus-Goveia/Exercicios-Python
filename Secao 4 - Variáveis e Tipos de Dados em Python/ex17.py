"""Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2,54 sendo C o comprimento em centímetros e
P o comprimento em polegadas."""

print('Conversor de Centímetros para polegadas.')
C = float(input('Digite a distancia em centímetros: '))
P = C / 2.54
print('{}cm é o mesmo que {} polegadas'.format(C, P))
print('FIM')
