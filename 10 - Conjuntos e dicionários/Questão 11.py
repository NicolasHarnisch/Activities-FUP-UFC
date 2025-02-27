# Questão 11
# Faça um programa que faça operações simples de números complexos:
# ◦ Crie e leia dois números complexos z e w, compostos por parte real e parte imaginária.
# ◦ Apresente a soma, subtração e produto entre z e w, nessa ordem, bem como o módulo de ambos. Cada operação deve ser feita em uma função diferente.

# Solução do exercício

import math

def criar_complexo():
    real = float(input())
    imaginario = float(input())
    return {"real": real, "imaginario": imaginario}

def soma(z, w):
    return {
        "real": z["real"] + w["real"],
        "imaginario": z["imaginario"] + w["imaginario"]
    }

def subtracao(z, w):
    return {
        "real": z["real"] - w["real"],
        "imaginario": z["imaginario"] - w["imaginario"]
    }

def produto(z, w):
    real = z["real"] * w["real"] - z["imaginario"] * w["imaginario"]
    imaginario = z["real"] * w["imaginario"] + z["imaginario"] * w["real"]
    return {"real": real, "imaginario": imaginario}

def modulo(z):
    return round(math.sqrt(z["real"] ** 2 + z["imaginario"] ** 2), 2)

def formatar_modulo(valor):
    return f"{valor:.2f}"

def main():
    z = criar_complexo()
    w = criar_complexo()
    print(soma(z, w))
    print(subtracao(z, w))
    print(produto(z, w))
    print(formatar_modulo(modulo(z)))
    print(formatar_modulo(modulo(w)))

if __name__ == "__main__":
    main()
