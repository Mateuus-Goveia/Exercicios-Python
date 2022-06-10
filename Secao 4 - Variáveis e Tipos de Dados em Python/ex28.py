"""Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos."""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
soma_dos_quadrados = n1 ** 2 + n2 ** 2 + n3 ** 2
print('A soma dos quadrados dos números {},{} e {} é igual a {}.'.format(n1, n2, n3, soma_dos_quadrados))
print('FIM')
