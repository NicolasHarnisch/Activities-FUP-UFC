# Questão 05
# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem crescente.

# Solução do exercício

def funcao(x):
    if x == 0:
        print(0)
    else:
        funcao(x - 1)
        print(x)

# Pra rodar o Programa
x = int(input(""))
funcao(x)