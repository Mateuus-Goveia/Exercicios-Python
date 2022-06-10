"""Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado."""

VH = float(input('Valor hora R$ '))
HR = float(input('Horas trabalhados: '))
SAL = VH * HR
BON = SAL + (SAL / 100 * 10)
print('Com uma bonificação de 10% você recebera {:.2f}'.format(BON))
print('FIM')
