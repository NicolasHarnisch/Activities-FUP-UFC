# Quesão 08
# Faça um programa que converta coordenadas polares para cartesianas:
# ◦ Crie e leia um ponto em coordenada polar, composto por raio (r) e ângulo (a) em radianos.
# ◦ Crie outro ponto, agora em coordenada cartesiana, composto por x e y, sabendo que x = r * cos(a) e y = r * sin(a).
# No programa principal, leia um ponto em coordenada polar, mostre esse ponto, e mostre as coordenadas do ponto convertido para o plano cartesiano. 
# A conversão deve ser feita em uma função.

# Solução do exercício

import math

def calcular(r, a):
    x = r * math.cos(a)
    y = r * math.sin(a)
    return {'x': x, 'y': y}

def main():
    r = float(input())
    a = float(input())

    pontos = {'r': r, 'a': a}
    print(pontos)

    ponto_cartesiano = calcular(r, a)
    print(ponto_cartesiano)


if __name__ == "__main__":
    main()
