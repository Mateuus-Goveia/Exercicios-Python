"""Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M sendo L o volume em litros e M o volume em
metros cúbicos."""

print('Conversor de metros cúbicos para litros.')
M = float(input('Digite aqui em m³: '))
L = M * 1000
print('{}m³ é o mesmo que {} litros'.format(M, L))
print('FIM')
