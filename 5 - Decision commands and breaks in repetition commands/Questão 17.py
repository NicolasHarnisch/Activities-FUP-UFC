# Questão 17
# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, 
# o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

# Solução do exercício

import math

def calcular_quadrado_cubo_raiz():
    while True:
        numero = int(input())
        
        if numero <= 0:
            break
        
        quadrado = numero ** 2
        cubo = numero ** 3
        raiz_quadrada = math.sqrt(numero)
        
        print(f"{quadrado:.2f}")
        print(f"{cubo:.2f}")
        print(f"{raiz_quadrada:.2f}")

calcular_quadrado_cubo_raiz()
