print('Bem Vindo a Loja do Rodrigo Najdek Vieira Rodrigues')
valor_produto = float(input('Entre com valor do produto: '))
qtd_produto = int(input('Entre com valor da quantidade: '))

if qtd_produto <= 9:  # Se a quantidade de produto selecionado for até 9
    desconto = 0.00  # 0%
elif 10 <= qtd_produto <= 99:  # Se a quantidade de produto selecionado for entre 10 e 99
    desconto = 0.05  # 5% = 5 / 100
elif 100 <= qtd_produto <= 999:  # Se a quantidade de produto selecionado for entre 100 e 999
    desconto = 0.10  # 10% = 10 / 100
else:  # Se a quantidade de produto selecionado não for entre 0 e 999 caíra nessa opção
    desconto = 0.15  # 15% = 15 / 100

valorSemDesconto = valor_produto * qtd_produto
valorComDesconto = (valor_produto * (1 - desconto)) * qtd_produto

print('O valor sem desconto foi: R$ {:.2f}'.format(valorSemDesconto))
print('O valor com desconto foi: R$ {:.2f} (desconto {}%)'.format(valorComDesconto, int(desconto * 100)))
