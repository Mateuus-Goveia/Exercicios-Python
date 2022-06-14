"""Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
Faça um programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro."""

V = float(input('Digite o valor do produto R$'))
print('Qual estado')
print('[1] para Minas Gerais 7% Imposto')
print('[2] para São Paulo 12% Imposto')
print('[3] para Rio de Janeiro 15% Imposto')
print('[4] para Mato Grosso do Sul 8% Imposto')
E = int(input('Digite aqui: '))
if E == 1:
    print(f'Em Minas Gerais o total vai ser R${V + (V / 100 * 7):.2f}')
elif E == 2:
    print(f'Em são paulo o total vai ser R${V + (V / 100 * 12)}:.2f')
elif E == 3:
    print(f'Em Rio de Janeiro o total vai ser R${V + (V / 100 * 15):.2f}')
elif E == 4:
    print(f'Em Mato Grosso do Sul o total vai ser R${V + (V / 100 * 8):.2f}')
else:
    print('Valor inválido.')
print('FIM')
