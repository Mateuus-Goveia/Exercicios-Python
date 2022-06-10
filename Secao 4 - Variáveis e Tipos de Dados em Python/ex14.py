"""Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * (Pi) / 180 sendo G o ângulo em graus e R em radianos e (Pi) = 3,14."""

print('Transformador de graus em radianos.')
G = float(input('Digite o ângulo: '))
R = G * 3.14 / 180
print('{}º é o mesmo que {:.2f}R'.format(G, R))
print('FIM')
