"""A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: trabalho de Laboratório: 2; avaliação semestral: 3; exame final: 5. Segundo o
resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de
recuperação (entre 3 4,9) ou se foi aprovado. Faça todas as verificações necessárias."""

print('-=' * 20)
print('\033[1;36mNOTAS DOS ALUNOS\033[m')
n_lab = float(input('Nota trabalho do laboratório: '))
n_ava = float(input('Nota da avaliação semestral: '))
n_exa = float(input('Nota do exame final: '))
media = ((n_lab * 2) + (n_ava * 3) + (n_exa * 5)) / (2+3+5)
if media < 3:
    print('Média do aluno \033[1;34m{}\033[m'.format(media))
    print('\033[1;31mALUNO REPROVADO\033[m')
elif 3 <= media < 5:
    print('Média do aluno \033[1;34m{}\033[m'.format(media))
    print('\033[1;33mALUNO DE RECUPERAÇÃO\033[m')
else:
    print('Média do aluno \033[1;34m{}\033[m'.format(media))
    print('\033[1;32mALUNO APROVADO\033[m')
print('Bons estudos !')
print('-=' * 20)
print('FIM')
