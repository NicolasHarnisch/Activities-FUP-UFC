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
