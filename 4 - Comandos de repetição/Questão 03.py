# Questão 03
# Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.

# Solução do exercício

soma = 0
for i in range(10):
    soma += float(input())
print(f"{soma:.2f}")
