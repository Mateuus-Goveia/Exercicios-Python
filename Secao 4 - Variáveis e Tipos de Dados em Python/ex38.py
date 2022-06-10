"""Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%"""

sal = float(input('Valor do Salário: '))
aum = sal + (sal / 100 * 25)
print('Seu novo salario com bonificação de 25% é de {}'.format(aum))
print('FIM')
