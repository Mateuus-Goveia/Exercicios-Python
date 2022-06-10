"""Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para o imposto de renda."""

dias = float(input('Dias trabalhados: '))
sal = 30 * dias
desc = sal / 100 * 8
total = sal - desc
print('Valor liquido a receber {}'.format(total))
print('FIM')
