# Questão 01
# Leia uma matriz 4 × 4 , conte e escreva quantos valores maiores que 10 ela possui.

# Solução do exercício

def main():
    num = []
    while len(num) < 16:
        for p in input().split():
            num.append(int(p))
    m = [[num[i*4+j] for j in range(4)] for i in range(4)]
    c = 0
    for i in range(4):
        for j in range(4):
            if m[i][j] > 10:
                c += 1
    print(c)
main()
