# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
listaIdade = []
listaAltura = []
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))

for i in range(5):
    idade = int(input("Digite sua idade: "))
    listaIdade.append(idade)
    altura = float(input("Digite sua altura: "))
    listaAltura.append(altura)

# usando método slice
# print(listaIdade[::-1])
# print(listaAltura[::-1])

# usando reverse
listaIdade.reverse()
listaAltura.reverse()
print(listaIdade)
print(listaAltura)