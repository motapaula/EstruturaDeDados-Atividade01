# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano bissexto.')
# elif ano % 400 == 0:
#     print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')