# Questão 15
# Faça um programa que leia duas matrizes A e B de tamanho 5 × 5 cada uma. Calcule a matriz C = A * B. 
# Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

# Solução do exercício

matriz_a = []
matriz_b = []
matriz_c = [[0] * 5 for _ in range(5)]

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz_a.append(linha)

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz_b.append(linha)

for i in range(5):
    for j in range(5):
        for k in range(5):
            matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

for linha in matriz_c:
    print(*linha)
