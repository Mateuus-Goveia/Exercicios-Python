"""Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

- O comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes."""

print('Descubra seu triângulo')
A = float(input('Digite o 1º lado do triângulo: '))
B = float(input('Digite o 2º lado do triângulo: '))
C = float(input('Digite o 3º lado do triângulo: '))
if A < B + C and B < A + C and C < A + B:
    if A == B and A == C:
        print('O TRIÂNGULO É EQUILÁTERO!')
    elif A != B and B != C and C != A:
        print('O TRIÂNGULO É ESCALENO!')
    else:
        print('O TRIÂNGULO É ISÓSCELES!')
else:
    print('OS LADOS NÃO FORMAM UM TRIÂNGULO')
print('FIM')
