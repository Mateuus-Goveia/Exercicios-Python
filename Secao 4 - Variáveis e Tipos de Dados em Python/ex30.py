"""Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares."""

# Cotação do dólar hoje: R$4,78
real = float(input('Digite o valor em real R$:'))
dolar = real / 4.78
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(real, dolar))
print('FIM')
