def dimensoesObjeto():
    while True:
        try:
            comprimento = int(input('1 - Digite o comprimento do objeto (em cm): '))
            largura = int(input('2 - Digite o comprimento do objeto (em cm): '))
            altura = int(input('3 - Digite o comprimento do objeto (em cm): '))
            volume = comprimento * largura * altura
            print('O volume do objeto é (em cm³): {}'.format(volume))
            if volume < 1000:
                return 10  # Se o valor do volume der menos de 1000 retorna o valor 10
            elif 1000 <= volume < 10000:
                return 20  # Se o valor do volume der entre 1000 e menos de 10000 retorna o valor 20
            elif 10000 <= volume < 30000:
                return 30  # Se o valor do volume der entre 10000 e menos de 30000 retorna o valor 30
            elif 30000 <= volume < 100000:
                return 50  # Se o valor do volume der entre 30000 e menos de 100000 retorna o valor 50
            else:
                print('Não aceitamos objetos com valores tão grandes (Só abaixo de 100000)')
                print('Entre com as dimensões desejados novamente')
                continue  # Volta para o início do while True se der valor maior ou igual de 100000
        except ValueError:  # Se o usuário digitar qualquer letra volta para a pergunta
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor entre com as dimensões desejados novamente')
# Fim da função dimensoesObjeto


def pesoObjeto():
    while True:
        try:
            peso0bj = float(input('Qual o peso do objeto (em kg): '))
            if peso0bj <= 0.1:
                return 1  # Se o usuário digitar o peso abaixo de 0.1 retorna o valor 1
            elif 0.1 <= peso0bj < 1:
                return 1.5  # Se o usuário digitar o peso entre 0.1 e menos de 1 retorna o valor 1.5
            elif 1 <= peso0bj < 10:
                return 2  # Se o usuário digitar o peso entre 1 e menos de 10 retorna o valor 1.5
            elif 10 <= peso0bj < 30:
                return 3  # Se o usuário digitar o peso entre 10 e menos de 30 retorna o valor 1.5
            else:
                print('Não aceitamos objetos tão pesados (Digite menos de 30)')
                print('Entre com o peso novamente')
                continue  # Volta para o início do while True se der valor maior ou igual de 30
        except ValueError:  # Se o usuário digitar qualquer letra volta para a pergunta
            print('Você digitou peso do objeto com valor não numérico')
            print('Por favor entre com o peso desejado novamente')
# Fim da função pesoObjeto


def rotaObjeto():
    while True:
        rotaObj = input('Selecione a rota: \n' +
                        ' RS - De Rio de Janeiro até São Paulo \n' +
                        ' SR - De São Paulo até Rio de Janeiro \n' +
                        ' BS - De Brasília até São Paulo \n' +
                        ' SB - De São Paulo até Brasília \n' +
                        ' BR - De Brasília até Rio de Janeiro \n' +
                        ' RB - Rio de Janeiro até Brasília \n' +
                        '>> ')
        rotaObj = rotaObj.upper()
        rotaObj = rotaObj.strip()
        if rotaObj == 'RS':
            return 1  # Se o usuário digitar 'rs' ou 'RS' retorna o valor 1
        elif rotaObj == 'SR':
            return 1  # Se o usuário digitar 'sr' ou 'SR' retorna o valor 1
        elif rotaObj == 'BS':
            return 1.2  # Se o usuário digitar 'bs' ou 'BS' retorna o valor 1
        elif rotaObj == 'SB':
            return 1.2  # Se o usuário digitar 'sb' ou 'SB' retorna o valor 1
        elif rotaObj == 'BR':
            return 1.5  # Se o usuário digitar 'br' ou 'BR' retorna o valor 1
        elif rotaObj == 'RB':
            return 1.5  # Se o usuário digitar 'rb' ou 'RB' retorna o valor 1
        else:
            print('Você digitou uma rota que não existe')
            print('Por favor entre com a rota desejada novamente')
            continue  # Volta para o início do while True se o usuário digitar qualquer coisa que não seja da tabela
# Fim da função rotaObjeto


# Programa Principal
print('Bem Vindo a Companhia de Logística Rodrigo Najdek Vieira Rodrigues S.A.')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print('Total a pagar (R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, dimensoes, peso, rota))
