# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
tempC = float(input('Qual a temperatura em Celsius? '))
tempF = float(tempC * 9 / 5 + 32)
print('A temperatura em Celsius é {:.1f}ºC, que equivale a {:.1f}ºF'.format(tempC, tempF))