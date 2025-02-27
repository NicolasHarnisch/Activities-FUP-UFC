# Questão 05
# Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). 
# A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .

# Solução do exercício

import math

raio = float(input())

volume = (4 / 3) * math.pi * (raio ** 3)
area = 4 * math.pi * (raio ** 2)

print(f"{volume:.2f}")
print(f"{area:.2f}")
