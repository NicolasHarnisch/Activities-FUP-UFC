# Questão 02
# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro n.

# Solução do exercício

def funcao(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * funcao(x - 1)

# Pra rodar o Programa
x = int(input(""))
y = funcao(x)
print(f"{y}")
