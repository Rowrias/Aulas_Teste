print('Bem Vindo a Lanchonete do Rodrigo Najdek Vieira Rodrigues')
print('*******************Cardápio****************')
print('|  Código |       Descrição       | Valor |')
print('|   100   |    Cachorro Quente    |  9,00 |')
print('|   101   | Cachorro Quente Duplo | 11,00 |')
print('|   102   |         X-Egg         | 12,00 |')
print('|   103   |       X-Salada        | 13,00 |')
print('|   104   |        X-Bacon        | 14,00 |')
print('|   105   |        X-Tudo         | 17,00 |')
print('|   200   |   Refrigerante Lata   |  5,00 |')
print('|   201   |     Chá Gelado        |  4,00 |')

total = 0
while True:
    codigo = int(input('Entre com o código desejado: '))
    if (codigo == 100):
        print('Você pediu um Cachorro-Quente no valor de 9,00')
        total += 9  # pega o valor que tinha no 'total' e soma com mais 9
    elif (codigo == 101):
        print('Você pediu um Cachorro-Quente Duplo no valor de 11,00')
        total += 11  # pega o valor que tinha no 'total' e soma com mais 11
    elif (codigo == 102):
        print('Você pediu um X-Egg no valor de 12,00')
        total += 12  # pega o valor que tinha no 'total' e soma com mais 12
    elif (codigo == 103):
        print('Você pediu um X-Salada no valor de 13,00')
        total += 13  # pega o valor que tinha no 'total' e soma com mais 13
    elif (codigo == 104):
        print('Você pediu um X-Bacon no valor de 14,00')
        total += 14  # pega o valor que tinha no 'total' e soma com mais 14
    elif (codigo == 105):
        print('Você pediu um X-Tudo no valor de 17,00')
        total += 17  # pega o valor que tinha no 'total' e soma com mais 17
    elif (codigo == 200):
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        total += 5  # pega o valor que tinha no 'total' e soma com mais 5
    elif (codigo == 201):
        print('Você pediu um Chá Gelado no valor de 4,00')
        total += 4  # pega o valor que tinha no 'total' e soma com mais 4
    else:  # Se o usuário digitar o código errado printa a mensagem abaixo
        print('Opção Inválida')
        continue  # Volta para o início do loop

    pedir_mais = input('Deseja pedir mais alguma coisa? \n- Sim (Digite a tecla (1)) \n- Não (Digite qualquer tecla)\n')
    if (pedir_mais == '1'):  # Se o usuário quiser pedir mais digite 1
        continue  # Volta para o início do loop
    else:  # Se digitar qualquer tecla printa o total a ser pago abaixo
        print('O total a ser pago é: {:.2f}'.format(total))
        break  # Saí do loop e encerra o programa
