# Questão 13
# Calcule as raízes da equação do 2o grau. Lembrando que: x = (−b± √∆)/(2a), onde ∆ = b2 − 4ac, e  ax2 + bx + c = 0 representa uma equação do 2o grau. A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Nao eh equacao do 2o grau".
# ◦ Se ∆ < 0 , não existe raiz real. Imprima a mensagem “Nao existe raiz real”.
# ◦ Se ∆ = 0 , existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
# ◦ Se ∆ > 0 , Imprima as duas raízes reais.

# Solução do exercício

import math

def calcular_raizes(a, b, c):
    if a == 0:
        print("Nao eh equacao do 2o grau")
        return

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("Nao existe raiz real")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"{raiz:.2f}")
        print("Raiz unica")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

        if raiz1 < raiz2:
            print(f"{raiz1:.2f}")
            print(f"{raiz2:.2f}")

        else:
            print(f"{raiz1:.2f}")
            print(f"{raiz2:.2f}")

a = float(input())
b = float(input())
c = float(input())

calcular_raizes(a, b, c)
