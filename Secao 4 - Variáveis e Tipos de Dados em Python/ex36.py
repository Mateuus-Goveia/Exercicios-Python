"""Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = (PI) * raio² * altura,
onde (PI) 3,141592."""

A = float(input('Digite aqui a altura do seu cilindro: '))
R = float(input('Digite aqui o raio do seu cilindro: '))
V = 2 * 3.141592 * R * (R + A)
print('A área do seu cilindro circular é {:.2f}'.format(V))
print('FIM')
