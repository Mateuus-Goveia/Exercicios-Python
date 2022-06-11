"""Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual."""

from datetime import date
a_atual = date.today().year
print('Descubra o ano do seu nascimento.')
idade = int(input('Digite sua idade: '))
a_nasc = a_atual - idade
print('{} é o ano do seu nascimento.'.format(a_nasc))
print('FIM')
