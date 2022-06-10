"""Sejam "a" e "b" os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
 "hipotenusa" = "a² + b² ** (1/2)". Faça um programa que receba os valores de "a" e "b" e calcule
   o valor da hipotenusa através da equação. Imprima o resultado dessa operação."""

print('Digite aqui os catetos do seu triângulo.')
cat1 = float(input('Primeiro: '))
cat2 = float(input('Segundo: '))
hip = (cat1 ** 2 + cat2 ** 2) ** (1/2)
print('A hipotenusa do seu triângulo é {:.3f}'.format(hip))
print('FIM')
