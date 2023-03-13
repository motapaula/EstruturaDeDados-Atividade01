# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

num = int(input("Digite um número inteiro qualquer: "))
def reverso_numero(num: int) -> int:
    str_num = str(num)
    reverse_num=str_num[::-1]
    return int(reverse_num)

print(reverso_numero(num))

# Com uma só linha
# print(int(input("Digite um número inteiro qualquer: "))[::-1])