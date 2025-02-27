# Questão 15
# Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, se sim escreva esses valores na tela.

# Solução do exercício

vetor = []
for _ in range(10):
    vetor.append(int(input()))

for i in range(10):
    for j in range(i + 1, 10):
        if vetor[i] == vetor[j]:
            print(vetor[i])
