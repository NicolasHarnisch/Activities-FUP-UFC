# Questão 30
# Faça um programa que receba uma palavra e a imprima de trás-para-frente.

# Solução do exercício

palavra = input()
for i in range(len(palavra)-1, -1, -1):
    print(palavra[i], end="")
