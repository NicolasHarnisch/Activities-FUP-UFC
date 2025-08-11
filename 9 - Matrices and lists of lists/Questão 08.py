# Quesão 08
# Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão acima da diagonal principal. 
# Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

# Solução do exercício

matriz = []

for _ in range(4):
    matriz.append([int(input()) for _ in range(4)])

soma = 0
for i in range(4):
    for j in range(i + 1, 4):
        soma += matriz[i][j]

print(soma)
