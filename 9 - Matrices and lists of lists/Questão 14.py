# Questão 14
# Faça um programa que leia duas matrizes A e B de tamanho 4 × 5 cada uma. Calcule a matriz C = A + B. 
# Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

# Solução do exercício

matriz_a = []
matriz_b = []
matriz_c = []

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz_a.append(linha)

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz_b.append(linha)

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(matriz_a[i][j] + matriz_b[i][j])
    matriz_c.append(linha)

for linha in matriz_c:
    print(*linha)
