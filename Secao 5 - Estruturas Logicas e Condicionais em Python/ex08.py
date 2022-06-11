nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if 0 <= media <= 10:
    print('A média do aluno é {}'.format(media))
else:
    print('Nota inválida tente novamente.')
print('FIM')
