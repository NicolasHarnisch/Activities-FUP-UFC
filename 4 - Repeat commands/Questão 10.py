# Questão 10
# Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule xn e retorne o resultado.

# Solução do exercício

def funcao(x, n):
    resultado = 1
    contador = 0
    while contador < n:
        resultado *= x
        contador += 1
    return resultado

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")