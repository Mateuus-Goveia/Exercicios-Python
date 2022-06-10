"""Leia um número inteiro e imprima a soma do sucessor de seu triplo com antecessor
de seu dobro"""

num = int(input('Digite um número: '))
A = num - 1
S = num + 1
T = S * 3
D = A * 2
soma = T + D
print('Seu número é o {}'.format(num))
print('Seu antecessor é o {} e o seu sucessor é o {}'.format(A, S))
print('A soma entre entre triplo do sucessor {} e o dobro do antecessor {}'
      ' é igual a {}.'.format(T, D, soma))
print('FIM')
