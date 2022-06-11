"""Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é invalido"""

num = float(input('Digite um número positivo: '))
if num > 0:
    raiz = num ** (1/2)
    print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
else:
    print('Seu número não é valido -.-')
print('FIM')
