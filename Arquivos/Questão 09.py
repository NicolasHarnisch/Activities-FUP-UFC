# Questão 09
# Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , 
# sendo G o ângulo em graus e R em radianos.

# Solução do exercício

import math

angulo_graus = float(input())
angulo_radianos = angulo_graus * math.pi / 180
print(f"{angulo_radianos:.2f}")
