# Questão 06
# Elabore uma função para calcular o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). 
# A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .

# Solução do exercício

import math

def funcao(x):
    volume = (4 / 3) * math.pi * (x ** 3)
    area = 4 * math.pi * (x ** 2)
    return volume, area