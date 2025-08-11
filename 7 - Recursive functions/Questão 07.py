# Questão 07
# Faça uma função recursiva que receba um número inteiro positivo par n e imprima todos os números pares de 0 até n em ordem crescente.

# Solução do exercício

def funcao(x):
    if x == 0:
        print(0)
    elif x % 2 == 0:
        funcao(x - 2)
        print(x)
    else:
        funcao(x - 1)

# Pra rodar o Programa
x = int(input(""))
funcao(x)