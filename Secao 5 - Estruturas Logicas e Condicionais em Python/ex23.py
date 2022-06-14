"""Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo:
1988, 1992, 1996."""

print("Vamos descobrir se o ano é bissexto.")
ano = int(input('Digite o ano: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('ANO BISSEXTO')
else:
    print('NÃO É UM ANO BISSEXTO.')
print('FIM')
