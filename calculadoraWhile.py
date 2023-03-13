print('Inicializando a Calculadora')
while True:
    operacao = input('Qual operação deseja realizar? (+), (-), (*), (/) ou digite (sair) para encerrar: ')
    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
    if (operacao == '+'):
        resultado = x + y
        print('{} {} {} = {}'.format(x, operacao, y, resultado))
        continue
    elif (operacao == '-'):
        resultado = x - y
        print('{} {} {} = {}'.format(x, operacao, y, resultado))
        continue
    elif (operacao == '*'):
        resultado = x * y
        print('{} {} {} = {}'.format(x, operacao, y, resultado))
        continue
    elif (operacao == '/'):
        resultado = x / y
        print('{} {} {} = {}'.format(x, operacao, y, resultado))
        continue
    elif (operacao == 'sair'):
        break
    else:
        print('Digite uma operação válida')
print('Finalizando o programa')
