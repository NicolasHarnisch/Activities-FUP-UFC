# Questão 14
# Faça um programa que preencha um vetor com 12 números reais aleatórios (uniformemente distribuídos no intervalo [-10, 10]), mostre esses números, 
# e calcule a quantidade de números negativos e a soma dos números positivos desse vetor. 
# A entrada para o programa é a semente dos números aleatórios.

# Solução do exercício

import random

s = int(input())
random.seed(s)

vetor = []
for i in range(12):
    vetor.append(random.uniform(-10, 10))

negativos = 0
soma_positivos = 0.0
for num in vetor:
    if num < 0:
        negativos += 1
    elif num > 0:
        soma_positivos += num

print(negativos)
print(f"{soma_positivos:.2f}")
