"""Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base."""

SAL = float(input('Salario mensal: '))
SAL_B = SAL + (SAL / 100 * 5)
IMP = SAL_B / 100 * 7
sal_liquido = SAL_B - IMP
print('Salario de {}'.format(SAL))
print('Bonificação salarial 5% {:.2f}'.format(SAL_B))
print('Imposto 7% {:.2f}'.format(IMP))
print('Total liquido: {:.2f}'.format(sal_liquido))
print('FIM')
