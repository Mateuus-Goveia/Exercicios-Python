"""Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:

- Ter pelo menos 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos."""

print('Descubra se você pode se aposentar.')
idade = int(input('Digite sua idade: '))
anos = int(input('Digite os anos de contribuição: '))
if idade >= 65 or anos >= 30:
    print('Parabéns você pode se aposentar.')
elif idade >= 60 and anos >= 25:
    print('Parabéns você pode se aposentar.')
else:
    print('Desculpa mas você ainda não pode se aposentar.')
