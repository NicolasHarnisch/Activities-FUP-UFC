# Questão 09
# Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão abaixo da diagonal principal. 
# Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

# Solução do exercício

matriz = [[int(input()) for _ in range(4)] for _ in range(4)]

soma = 0
for i in range(4):
    for j in range(i):
        soma += matriz[i][j]

print(soma)
