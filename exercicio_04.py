# ----- Início das Variáveis Globais -----
lista_peca = []
codigo_peca = 0
# ----- Fim das Variáveis Globais -----


# ----- Início de cadastrarPeca() -----
def cadastrarPeca(peca):
    print('------------------------')
    print('Você selecionou a Opção de Cadastrar Peça')
    print('Código da Peça: {:0>3}'.format(peca))
    nome = input('Por favor entre com o NOME do peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    preco = int(input('Por favor entre com o VALOR(R$) da peça: '))
    dicionario_peca = {'codigo': peca,
                       'nome': nome,
                       'fabricante': fabricante,
                       'preco': preco}
    lista_peca.append(dicionario_peca.copy())
# ----- Fim de cadastrarPeca() -----


# ----- Início de consultarPeca() -----
def consultarPeca():
    print('------------------------')
    print('Você selecionou a opção Consultar Peças')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1 - Consultar Todas as Peças\n' +
                                '2 - Consultar Peças por Código\n' +
                                '3 - Consultar Peças por Fabricante\n' +
                                '4 - Retornar\n' +
                                '>> ')
        if opcao_consultar == '1':
            print('Você selecionou a opção Consultar todas as Peças')
            for peca in lista_peca:  # peca vai varrer toda a lista de peca
                print('------------------------')
                for key, value in peca.items():  # Varrer todos os conjutos chaves e valor do dicionario peca
                    print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '2':
            print('Você selecionou a opção Consultar por Código')
            valor_desejado = int(input('Entre com o Código desejado: '))
            for peca in lista_peca:
                if peca['codigo'] == valor_desejado:  # O valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------')
                    for key, value in peca.items():  # Varrer todos os conjutos chaves e valor do dicionário peça
                        print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '3':
            print('Você selecionou a opção Consultar Peças por Fabricante')
            valor_desejado = input('Entre com o Fabricante desejado: ')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado:  # o valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------')
                    for key, value in peca.items():  # Varrer todos os conjutos chaves e valor do dicionário peça
                        print('{}: {}'.format(key, value))
                print('------------------------')
        elif opcao_consultar == '4':
            return  # Sai da função consultar_peca e volta para o Main
        else:
            print('Opção Inválida, Tente Novamente')
            continue  # Volta para o início do laço
# ----- Fim de consultarPeca() -----


# ----- Início de remover_produto() -----
def removerPeca():
    print('------------------------')
    print('Você Selecionou a Opção de Remover Peça')
    valor_desejado = int(input('Digite o codigo da peça a ser removida: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:  # O valor do campo código desse dicionário é igual o valor desejado
            lista_peca.remove(peca)
            print('Produto Removido')
# ----- Fim de remover_produto() -----


# ----- Início de Main -----
print('Bem-vindo ao Controle de Estoque da Bicicletaria do Rodrigo Najdek Vieira Rodrigues')
while True:
    print('------------------------')
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1 - Cadastrar Peças\n' +
                            '2 - Consultar Peças\n' +
                            '3 - Remover Peças\n' +
                            '4 - Sair\n' +
                            '>> ')
    if opcao_principal == '1':  # Se selecionar essa opção entra na função cadastrarPeca(codigo_peca)
        codigo_peca += 1
        cadastrarPeca(codigo_peca)
    elif opcao_principal == '2':  # Se selecionar essa opção entra na função consultarPeca()
        consultarPeca()
    elif opcao_principal == '3':  # Se selecionar essa opção entra na função removerPeca()
        removerPeca()
    elif opcao_principal == '4':
        break  # Encerra o laço principal e o programa encerra
    else:
        print('Opção Inválida, Tente Novamente')
        continue  # Se digitar qualquer outra tecla volta para o início do laço
print('------------------------')
print('Encerrando o programa')
# ----- Fim de Main -----
