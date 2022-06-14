"""Leia a distância em Km e a quantidade de litros de gasolina consumimos por um carro
em um percurso, calcule o consume em Km/l e escreva uma mensagem de acordo com
a tabela abaixo

                Consumo       (Km/l)     MENSAGEM
                menor que       8        Venda o carro!
                entre         8 e 14     Econômico!
                maior que      12        Super econômico!"""

print('Consumo do automóvel.')
D = float(input('Digite a distância percorrida Km'))
L = float(input('Gasolina consumida (litros): '))
C = D / L
print(f'{C}Km/l')
if C < 8:
    print('Venda o carro!')
elif 7 > C < 15:
    print('Econômico!')
else:
    print('Super econômico!')
print('FIM')
