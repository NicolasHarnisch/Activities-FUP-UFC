# Questão 19
# Faça um programa que gere uma matriz m × n de inteiros aleatórios (gerados a partir de uma semente), 
# calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. 
# A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como entrada para o programa.

# Solução do exercício

import random

m = int(input())
n = int(input())
random.seed(int(input()))
inicio = int(input())
final = int(input())

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(random.randint(inicio, final))
    matriz.append(linha)

for i in range(m):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()

for i in range(m):
    if i % 2 == 0:  
        soma = 0
        contador = 0
        for j in range(n):
            soma += matriz[i][j]
            contador += 1
        media = soma / contador
        print(f"{media:.2f}")
    else: 
        negativos_divisores_de_tres = 0
        for j in range(n):
            if matriz[i][j] < 0 and matriz[i][j] % 3 == 0:
                negativos_divisores_de_tres += 1
        print(negativos_divisores_de_tres)
