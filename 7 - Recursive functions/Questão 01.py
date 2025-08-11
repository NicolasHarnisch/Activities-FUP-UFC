# Questão 01
# Crie uma função recursiva que receba um número inteiro positivo n e calcule o somatório dos números de 1 até n.

# Solução do exercício

def funcao(x):
    if x == 1:
        return 1
    else:
        return x + funcao(x - 1)

# Pra rodar o Programa
x = int(input(""))
y = funcao(x)
print(f"{y}")