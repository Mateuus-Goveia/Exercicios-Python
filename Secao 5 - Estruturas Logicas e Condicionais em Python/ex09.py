salario = float(input('Digite aqui seu salario: '))
emprestimo = float(input('Valor do empréstimo: '))
n_parcelas = int(input('Numero de parcelas: '))
v_parcelas = float(emprestimo / n_parcelas)
if v_parcelas < salario / 100 * 20:
    print('Empréstimo APROVADO !')
else:
    print('Empréstimo RECUSADO !')
print('FIM')
