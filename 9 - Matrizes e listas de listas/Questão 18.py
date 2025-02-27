# Questão 18
# Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de uma semente dada como entrada. 
# Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. 
# Imprima a matriz original e a matriz transformada. Não use nenhum comando de decisão (se/então/senão).

# Solução do exercício

import random

s = int(input())
random.seed(s)

matriz = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
triangular = [[matriz[i][j] * (i >= j) for j in range(5)] for i in range(5)]

for i in range(5):
    linha = ""
    for j in range(5):
        linha += str(matriz[i][j]) + " "
    print(linha.strip())

print()

for i in range(5):
    linha = ""
    for j in range(5):
        linha += str(triangular[i][j]) + " "
    print(linha.strip())
