"""Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o número lido não for maior que zero, o programa terminará com a
mensagem "Número inválido"."""

num = int(input("Digite um número inteiro positivo: "))
if num > 0:
    U = num // 1 % 10
    D = num // 10 % 10
    C = num // 100 % 10
    M = num // 1000 % 10
    print(U + D + C + M)
else:
    print("Número inválido")
print("FIM")
