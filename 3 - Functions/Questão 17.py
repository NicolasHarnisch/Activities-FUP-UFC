# Questão 17
# Escreva uma função que, dadas as coordenadas x e y de pontos no R2 e retorne sua distância para a origem (0, 0).

# Solução do exercício

import math

def funcao(x1,x2):
    return math.sqrt(x1**2 + x2**2)

# Pra rodar o Programa
x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1, x2)
print(f"{y:.2f}")