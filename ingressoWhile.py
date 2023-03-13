total = 0
dinheiro = 0

while True:
    idade = input('Digite a sua idade: ')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    elif idade < 12:
        ingresso = 15
    else:
        ingresso = 30
    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total de arrecadado: {}'.format(dinheiro))
print('Média arrecadado: {}'.format(media))
