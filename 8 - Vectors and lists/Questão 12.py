# Questão 12
# Faça uma uma função que receba um vetor com a nota de 15 alunos e e retorne tanto a média geral quanto o desvio padrão (populacional).

# Solução do exercício

import math

def funcao(x):
    soma = 0
    for nota in x:
        soma += nota
    media = soma / 15

    soma_quad = 0
    for nota in x:
        soma_quad += (nota - media) ** 2
    desvio = math.sqrt(soma_quad / 15)

    return media, desvio

# Pra rodar o programa
x = []
for i in range(15):
    x.append(float(input("")))
y1, y2 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")