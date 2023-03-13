valor = int(input('Digite o valor em R$ '))

while True:
    if (valor >= 100):
        cedulas100 = valor // 100
        valor = valor % 100
        print('Cédulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if (valor >= 50):
        cedulas50 = valor // 50
        valor = valor % 50
        print('Cédulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if (valor >= 20):
        cedulas20 = valor // 20
        valor = valor % 20
        print('Cédulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if (valor >= 10):
        cedulas10 = valor // 10
        valor = valor % 10
        print('Cédulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if (valor >= 5):
        cedulas5 = valor // 5
        valor = valor % 5
        print('Cédulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if (valor >= 1):
        cedulas1 = valor // 1
        valor = valor % 1
        print('Cédulas de 1: {}'.format(cedulas1))
        break
