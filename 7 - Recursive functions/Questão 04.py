# Questão 04
# Crie uma função recursiva que receba dois inteiros positivos n e k e calcule nk.

# Solução do exercício

def funcao(x1, x2):
    if x2 == 0:
        return 1
    else:
        return x1 * funcao(x1, x2 - 1)

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")