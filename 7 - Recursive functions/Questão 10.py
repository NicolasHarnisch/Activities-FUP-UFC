# Questão 10
# Escreva uma função recursiva que calcule a sequência dada por: F(1) = 1; F(2) = 2; e F(n) = 2*F(n − 1) + 3*F(n − 2).

# Solução do exercício

def funcao(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return 2 * funcao(x - 1) + 3 * funcao(x - 2)

# Pra rodar o Programa
x = int(input(""))
y = funcao(x)
print(f"{y}")