# Questão 23
# Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.

# Solução do exercício

def primo(n):
    if abs(n) < 2: 
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if abs(n) % i == 0:
            return False
    return True

vetor = [int(input()) for _ in range(10)]

for i in range(len(vetor)):  
    if primo(vetor[i]):
        print(vetor[i])
        print(i)
