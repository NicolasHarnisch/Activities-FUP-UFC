# Questão 25
# Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + … + (n2 + 1)/(n + 3)

# Solução do exercício

def funcao(n):
    soma = 0
    for i in range(1, n + 1):
        soma += (i**2 + 1) / (i + 3)
    return soma

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y:.2f}")