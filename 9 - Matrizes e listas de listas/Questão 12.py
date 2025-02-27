# Questão 12
# Leia uma matriz 4 × 4. Calcule e imprima sua transposta. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

# Solução do exercício

matriz = [[int(input()) for _ in range(4)] for _ in range(4)]

transposta = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        transposta[j][i] = matriz[i][j]

for linha in transposta:
    print(*linha)
