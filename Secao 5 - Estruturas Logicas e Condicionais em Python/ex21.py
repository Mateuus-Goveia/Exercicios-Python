"""Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero)
Opção:"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('Escolha a opção:')
print('[1] Soma de 2 números.')
print('[2] Diferença entre 2 números.)')
print('[3] Produto entre 2 números.')
print('[4] Divisão entre 2 números.')
Opc = int(input('Opção: '))
if Opc == 1:
    print(f'{num1 + num2}')
elif Opc == 2:
    if num1 > num2:
        print(f'{num1 - num2}')
    elif num2 > num1:
        print(f'{num2 - num1}')
    else:
        print('Os números são iguais.')
elif Opc == 3:
    print(f'{num1 * num2}')
elif Opc == 4:
    if num1 > 0 and num2 > 0:
        print(f'{num1 / num2}')
else:
    print('Opção inválida')
print('FIM')
