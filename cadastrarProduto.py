# ----- Início das Variáveis Globais -----
lista_produto = []
codigo_produto = 0
# ----- Fim das Variáveis Globais -----


# ----- Início de cadastrar_produto() -----
def cadastrar_produto(codigo):
    print('Bem-vindo ao menu de Cadastrar Produto')
    print('Código do Produto: {}'.format(codigo))
    nome = input('Entre com o NOME do produto: ')
    fabricante = input('Entre com o FABRICANTE do produto: ')
    preco = int(input('Entre com o PREÇO(R$) do produto: '))
    dicionario_produto = {'codigo'     : codigo,
                          'nome'       : nome,
                          'fabricante' : fabricante,
                          'preco'      : preco}
    lista_produto.append(dicionario_produto.copy())
# ----- Fim de cadastrar_produto() -----


# ----- Início de consultar_produto() -----
def consultar_produto():
    print('Bem-vindo ao menu de Consultar Produto')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1 - Consultar Todos os Produto\n' +
                                '2 - Consultar Produtos por CÓDIGO\n' +
                                '3 - Consultar Produto por FABRICANTE\n' +
                                '4 - Retornar\n' +
                                '>> ')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar TODOS os Produtos')
            for produto in lista_produto:  # Produto vai varrer toda a lista de produtos
                print('------------------------')
                for key, value in produto.items():  # Varrer todos os conjutos chaves e valor do dicionario produto
                    print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar por CÓDIGO')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for produto in lista_produto:
                if produto['codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------')
                    for key, value in produto.items():  # Varrer todos os conjutos chaves e valor do dicionario produto
                        print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Produtos(s) por FABRICANTE')
            valor_desejado = input('Entre com o FABRICANTE desejado: ')
            for produto in lista_produto:
                if produto['fabricante'] == valor_desejado:  # o valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------')
                    for key, value in produto.items():  # Varrer todos os conjutos chaves e valor do dicionario produto
                        print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '4':
            return  # Sai da função consultar_produto e volta para o Main
        else:
            print('Opção Inválida, Tente Novamente')
            continue  # Volta para o início do laço
# ----- Fim de consultar_produto() -----


# ----- Início de remover_produto() -----
def remover_produto():
    print('Bem-vindo ao menu de Remover Produto')
    valor_desejado = int(input('Entre com o CÓDIGO do produto que deseja remover: '))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual o valor desejado
            lista_produto.remove(produto)
            print('Produto Removido')
# ----- Fim de remover_produto() -----


# ----- Início de Main -----
print('Bem-vindo a Mercearia do Renan Portela Jorge')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n' +
                            '1 - Cadastrar Produto\n' +
                            '2 - Consultar Produtos(s)\n' +
                            '3 - Remover Produto\n' +
                            '4 - Sair\n' +
                            '>> ')
    if opcao_principal == '1':
        codigo_produto += 1
        cadastrar_produto(codigo_produto)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        break  # Encerra o laço principal e o programa acaba
    else:
        print('Opção Inválida, Tente Novamente')
        continue  # Volta para o início do laço
# ----- Fim de Main -----
