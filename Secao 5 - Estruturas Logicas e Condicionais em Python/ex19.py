"""Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou
5, mas não simultaneamente pelos dois."""

num = int(input('Digite um número: '))
if num % 3 == 0 and num % 5 != 0:
    print(f'{num} É DIVISÍVEL POR 3 MAS NÃO POR 5')
elif num % 5 == 0 and num % 3 != 0:
    print(f'{num} É DIVISÍVEL POR 5 MAS NÃO POR 3')
else:
    print('Não corresponde aos critérios.')
print('FIM')
