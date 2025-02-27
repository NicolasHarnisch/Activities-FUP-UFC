# Questão 04
# Leia uma matriz 4 × 4, imprima a matriz e retorne a localização (linha e coluna) do maior valor.

# Solução do exercício

def main():
    matriz = []
    nums = []

    while len(nums) < 16:
        nums.extend(map(int, input().split()))

    for i in range(4):
        matriz.append(nums[i * 4:(i + 1) * 4])

    for linha in matriz:
        print(*linha)

    maior = matriz[0][0]
    lin_maior, col_maior = 0, 0

    for i in range(4):
        for j in range(4):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                lin_maior, col_maior = i, j

    print(lin_maior)
    print(col_maior)
    print(maior)

main()
