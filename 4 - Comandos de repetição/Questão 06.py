# Questão 06
# Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.

# Solução do exercício

N = int(input())
soma = 0
for i in range(1, N + 1):
    soma += i
print(soma)
