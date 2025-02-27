# Questão 28
# Faça um algoritmo que leia um número inteiro e imprima seus divisores.

# Solução do exercício

numero = int(input())

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
