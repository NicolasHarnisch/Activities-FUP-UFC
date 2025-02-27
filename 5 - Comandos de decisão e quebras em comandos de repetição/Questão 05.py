# Questão 05
# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

# Solução do exercício

import math

def calcular_raiz():
    numero = float(input())
    if numero > 0:
        print(f"{math.sqrt(numero):.2f}")
    else:
        print("Numero invalido")

calcular_raiz()
