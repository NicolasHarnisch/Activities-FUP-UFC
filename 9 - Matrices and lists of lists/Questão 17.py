# Questão 17
# Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada coluna pelo maior elemento daquela coluna que seja primo. 
# Caso a coluna não possua um número primo, divida a coluna pelo menor número da coluna. Escreva a matriz original e a modificada.

# Solução do exercício

import math


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True


matriz = []
for i in range(12):
    linha = []
    for j in range(13):
        linha.append(int(input()))
    matriz.append(linha)

modificada = [linha.copy() for linha in matriz]

for j in range(len(modificada[0])):
    maior_primo = None
    menor_numero = None

    for i in range(len(modificada)):
        valor = modificada[i][j]
        if eh_primo(valor):
            if maior_primo is None or valor > maior_primo:
                maior_primo = valor
        if menor_numero is None or valor < menor_numero:
            menor_numero = valor

    if maior_primo is not None:
        divisor = maior_primo
    else:
        divisor = menor_numero

    for i in range(len(modificada)):
        modificada[i][j] /= divisor


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]}", end=" ")
    print()

for i in range(len(modificada)):
    for j in range(len(modificada[i])):
        print(f"{modificada[i][j]}", end=" ")
    print()