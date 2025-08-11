# Questão 03
# Escreva uma função recursiva que calcule a soma dos primeiros n cubos: S(n) = 13 + 23 + … + n3.

# Solução do exercício

def funcao(x):
    if x == 1:
        return 1**3
    else:
        return x**3 + funcao(x - 1)

# Pra rodar o Programa
x = int(input(""))
y = funcao(x)
print(f"{y}")