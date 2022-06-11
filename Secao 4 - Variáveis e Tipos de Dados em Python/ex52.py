"""Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um,
ganharia do prêmio com base no valor investido."""

valor_premio = float(input('Digite o valor do premio: '))

nome1 = str(input('Nome do primeiro amigo: ')).title().strip()
aposta1 = float(input(f'Digite a aposta do {nome1}: '))

nome2 = str(input('Nome do segundo amigo: ')).title().strip()
aposta2 = float(input(f'Digite a aposta do {nome2}: '))

nome3 = str(input('Nome do terceiro amigo: ')).title().strip()
aposta3 = float(input(f'Digite a aposta do {nome3}: '))

total_apostas = aposta1 + aposta2 + aposta3  # equivale a 100% das apostas
porcentagem1 = aposta1 * 100 / total_apostas
porcentagem2 = aposta2 * 100 / total_apostas
porcentagem3 = aposta3 * 100 / total_apostas

print(f'{nome1} Irá receber {valor_premio / 100 * porcentagem1}')
print(f'{nome2} Irá receber {valor_premio / 100 * porcentagem2}')
print(f'{nome3} Irá receber {valor_premio / 100 * porcentagem3}')
print('FIM')
