"""Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180 / (Pi) sendo G o ângulo em graus e R em radianos e (Pi) = 3,14."""

print('Conversor radianos em graus.')
R = float(input('Digite em Radianos: '))
G = R * 180 / 3.14
print('{}R é o mesmo que {:.2f}º'.format(R, G))
print('FIM')
