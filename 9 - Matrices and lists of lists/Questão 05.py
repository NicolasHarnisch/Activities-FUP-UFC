# Questão 05
# Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, 
# escrever a localização (linha e coluna) ou uma mensagem de "Nao encontrado".

# Solução do exercício

matriz = [[int(input()) for _ in range(5)] for _ in range(5)]

n = int(input())
encontrado = False

for i in range(5):
    for j in range(5):
        if matriz[i][j] == n:
            print(i)
            print(j)
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("Nao encontrado")
