def volumeFeijoada():
    print('--- Menu 1 de 3 - Volume Feijoada ---')
    while True:
        try:
            volumeF = int(input('digite a quantidade desejada (ml): '))
            if (volumeF >= 300) and (volumeF <= 5000):
                return volumeF * 0.08
            else:
                print('Pare de digitar valores abaixo de 300 ou acima de 5000')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')


def opcaoFeijoada():
    print('--- Menu 2 de 3 - Opção Feijoada ---')
    while True:
        opcaoF = input('Qual opção de feijoada deseja \n' +
                       'b- Básica (Feijão + paiol + costelinha \n' +
                       'p- Premium (Feijão + paiol + costelinha + partes de porco) \n' +
                       's- Suprema (Feijão + paiol + costelinha + partes de porco + charque \n' +
                       '>> ')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Para de digitar opções que não seja b/p/s')
            continue


def acompanhamentoFeijoada():
    print('--- Menu 3 de 3 - Acompanhamento Feijoada ---')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja mais algum adicional: \n' +
                                '0 - Não desejo mais acompanhamentos (encerrar pedido) \n' +
                                '1 - 200g de arroz \n' +
                                '2 - 150g de farofa especial \n' +
                                '3 - 100g de couve cozida \n' +
                                '4 - 1 laranja descascada \n' +
                                '>> ')
        if acompanhamentoF == '0':
            return acumulador
        elif acompanhamentoF == '1':
            acumulador = acumulador + 5
            continue
        elif acompanhamentoF == '2':
            acumulador = acumulador + 6
            continue
        elif acompanhamentoF == '3':
            acumulador = acumulador + 7
            continue
        elif acompanhamentoF == '4':
            acumulador = acumulador + 3
            continue
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3/4!')


# main
print('--- Bem-vindo ao programa de feijoada do Rodrigo Najdek')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = (volume * opcao) + acompanhamento
print('O total ficou: {:.2f} (Volume: R$ {:.2f}, Opção: R$ {:.2f}, '
      'Acompanhamento: R$ {:.2f}'.format(total, volume, opcao, acompanhamento))
