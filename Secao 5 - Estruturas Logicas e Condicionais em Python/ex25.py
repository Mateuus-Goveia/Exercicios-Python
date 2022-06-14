"""Calcule as raízes da equação de 2º grau.
Lembrando que:
x = ((-b +- delta ** (1/2)) / 2a

delta = B² - 4ac"""

# Calculando o Delta
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = b ** 2 - 4 * a * c
print(f'delta é = {delta}')
# Descobrindo as raízes
if delta < 0:
    print('Não existe raiz')
elif delta == 0:
    raiz = (-b + delta ** (1/2)) / 2 * a
    print(f'existe uma raiz real {raiz:.2f}')
else:
    raiz1 = (-b + delta ** (1/2)) / 2 * a
    raiz2 = (-b - delta ** (1/2)) / 2 * a
    print(f'Raiz 1 {raiz1:.2f} e Raiz 2 {raiz2:.2f}')
print('FIM')
