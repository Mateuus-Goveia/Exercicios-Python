p1 = float(input('Digite a nota da primeira prova: '))
p2 = float(input('Digite a nota da segunda prova: '))
p3 = float(input('Digite a nota da terceira prova: '))
media = (p1 + p2 + (p3 * 2)) / 4
if media >= 60:
    print('A média do aluno é de {}'.format(media))
    print('ALUNO APROVADO !')
else:
    print('A média do aluno é de {}'.format(media))
    print('ALUNO REPROVADO')
print('FIM')
