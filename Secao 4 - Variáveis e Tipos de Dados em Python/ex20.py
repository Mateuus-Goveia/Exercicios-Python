"""Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é L = K / 0,45 sendo K a massa em quilogramas e L a massa em libras."""

K = float(input('Digite aqui em Kg: '))
L = K / 0.45
print('{}kg é o mesmo que {:.2f} libras'.format(K, L))
print('FIM')
