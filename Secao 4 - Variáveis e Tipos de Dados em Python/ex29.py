"""Leia quatro notas, calcule a média aritmética e imprima o resultado."""

n1 = float(input('Digite aqui a nota: '))
n2 = float(input('Digite aqui a nota: '))
n3 = float(input('Digite aqui a nota: '))
n4 = float(input('Digite aqui a nota: '))
media = (n1 + n2 + n3 + n4) / 4
print('A média dos valores {},{},{} e {} é igual a {}'.format(n1, n2, n3, n4, media))
print('FIM')
