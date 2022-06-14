"""Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:

Categoria     idade
Infantil A    5 a 7
Infantil B    8 a 10
Juvenil  A    11 a 13
Juvenil  B    14 a 17
Sênior        maiores de 18 anos"""

print('Classificador natação.')
idade = int(input('Digite a idade: '))
if 5 <= idade < 8:
    print(f'idade {idade}')
    print('Categoria Infantil A')
elif 8 <= idade < 11:
    print(f'idade {idade}')
    print('Categoria Infantil B')
elif 11 <= idade < 14:
    print(f'idade {idade}')
    print('Categoria Juvenil B')
elif 14 <= idade < 18:
    print(f'idade {idade}')
    print('Categoria Juvenil A')
elif idade >= 18:
    print(f'idade {idade}')
    print('Categoria Sênior')
else:
    print('Não existe uma categoria nessa faixa de idade.')
print('FIM')
