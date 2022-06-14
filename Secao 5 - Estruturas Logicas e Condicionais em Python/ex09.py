"""Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima "Empréstimo não concedido", caso
contrário imprima "Empréstimo concedido"."""

sal = float(input('Digite aqui seu salario: '))
emp = float(input('Valor do empréstimo: '))
n_par = int(input('Numero de parcelas: '))
v_par = float(emp / n_par)
if v_par < sal / 100 * 20:
    print('Empréstimo APROVADO !')
else:
    print('Empréstimo RECUSADO !')
print('FIM')
