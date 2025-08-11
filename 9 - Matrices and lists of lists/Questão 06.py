# Questão 06
# Leia duas matrizes 4 × 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas.

# Solução do exercício

matriz1 = []
matriz2 = []

for i in range(4):
    linha = [int(input()) for _ in range(4)]
    matriz1.append(linha)

for i in range(4):
    linha = [int(input()) for _ in range(4)]
    matriz2.append(linha)

matriz3 = [[max(matriz1[i][j], matriz2[i][j]) for j in range(4)] for i in range(4)]

for linha in matriz3:
    print(*linha)
