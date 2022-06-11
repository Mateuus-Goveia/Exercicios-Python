A = float(input('Digite a altura: '))
print('Digite o sexo')
print('[1] para masculino')
print('[2] para feminino')
S = float(input('Digite aqui: '))
if S == 1:
    IMC = (72.7 * A) - 58
    print('Seu peso ideal é {:.2f}'.format(IMC))
elif S == 2:
    IMC = (62.1 * A) - 44.7
    print('Seu peso ideal é {:.2f}'.format(IMC))
else:
    print('Valor do sexo invalido tente novamente.')
print('FIM')
