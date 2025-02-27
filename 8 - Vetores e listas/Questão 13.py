# Questão 13
# Faça uma função que receba um vetor com as notas de vários alunos, e retorne a média geral, o desvio padrão (populacional), e quantos alunos estão com nota menor que 7.0.

# Solução do exercício

import math

def funcao(vetor):
    n = len(vetor)
    soma = 0
    for nota in vetor:
        soma += nota
    media = soma / n
    
    soma_quad = 0
    menor_7 = 0
    for nota in vetor:
        soma_quad += (nota - media) ** 2
        if nota < 7.0:
            menor_7 += 1
            
    desvio = math.sqrt(soma_quad / n)
    return media, desvio, menor_7

# Pra rodar o programa
x = []
for i in range(15):
    x.append(float(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3}")