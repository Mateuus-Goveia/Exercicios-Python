"""Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos."""

print('Transformador de segundos em horas e minutos.')
S = int(input('Digite quantos segundos: '))
M = S / 60
H = S / 3600
print('{} segundos é o mesmo que {:.2f} hora(s)'.format(S, H))
print('{} segundos é o mesmo que {:.2f} minuto(s).'.format(S, M))
print('FIM')
