# Questão 07
# Gerar e imprimir uma matriz A de tamanho 10 × 10 , onde seus elementos são da forma:
# ◦ A[i][j] = 2 * i + 7 * j - 2, se i < j;
# ◦ A[i][j] = 3 * i 2 − 1, se i = j;
# ◦ A[i][j] = 4 * i 3 − 5 * j 2 + 1, se i > j.

# Solução do exercício

matriz = [[(2 * i + 7 * j - 2) if i < j else (3 * i ** 2 - 1) if i == j else (4 * i ** 3 - 5 * j ** 2 + 1) for j in range(10)] for i in range(10)]

for linha in matriz:
    print(*linha)
