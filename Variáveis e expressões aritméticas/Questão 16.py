# Questão 16
# Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0, 0).

# Solução do exercício

import math

x = float(input())
y = float(input())

distancia = math.sqrt(x**2 + y**2)

print(f"{distancia:.2f}")
