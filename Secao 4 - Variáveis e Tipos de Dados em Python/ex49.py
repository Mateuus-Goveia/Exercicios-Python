"""Faça um programa para leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do término da mesma."""

h = int(input('Hora: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
d = int(input('Duração em Segundos: '))
hf = h + (d // 3600)
mf = m + ((d % 3600) // 60)
sf = s + ((d % 3600) % 60)
print(f'A experiencia vai terminar em {hf:0>2}:{mf:0>2}:{sf:0>2}')
print('FIM')
