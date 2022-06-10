"""Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

● o total a pagar com desconto de 10%;
● o valor de cada parcela, no parcelamento de 3x sem juros;
● a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
● a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)"""

valor = float(input('Valor do produto R$'))
total_a_pagar = valor - (valor / 100 * 10)
parcela_2 = valor / 2
parcela_3 = valor / 3
comissao_a_vista = total_a_pagar / 100 * 5
comissao_parcela = valor / 100 * 5
print('Total a pagar com 10% de desconto {:.2f}'.format(total_a_pagar))
print('Valor da parcela em 2x sem juros {:.2f}'.format(parcela_2))
print('Valor da parcela em 3x sem juros {:.2f}'.format(parcela_3))
print('Comissão do vendedor a vista {:.2f}'.format(comissao_a_vista))
print('Comissão do vendedor parcelado {:.2f}'.format(comissao_parcela))
print('FIM')
