"""Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo."""

dist = float(input('Digite a distancia que deseja alcançar em metros: '))
degrau = float(input('Digite a altura do degrau em metros: '))
q_degrau = dist / degrau
print('Você precisara subir {} degraus para chegar na distance de {} metros.'.format(q_degrau, dist))
print('FIM')
