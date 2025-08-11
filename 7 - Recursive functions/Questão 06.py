# Questão 06
# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem decrescente.

# Solução do exercício

def funcao(x):
    if x >= 0:
        print(x)
        funcao(x - 1)

# Pra rodar o Programa
x = int(input(""))
funcao(x)