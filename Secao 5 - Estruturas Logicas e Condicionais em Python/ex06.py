num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
if num1 > num2:
    diferenca = num1 - num2
    print('{} É maior que {} com a diferença de {} numeros!!'.format(num1, num2, diferenca))
elif num2 > num1:
    diferenca = num2 - num1
    print('{} É maior que {} com a diferença de {} numeros!!'.format(num2, num1, diferenca))
else:
    print('Os números são iguais :(')
print('FIM')
