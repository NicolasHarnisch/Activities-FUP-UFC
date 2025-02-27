# Questão 04
# Faça um programa que leia 10 inteiros e imprima sua média.

# Solução do exercício

soma = 0
for i in range(10):
    soma += float(input())
    media = soma / 10
print(f"{media:.2f}")
