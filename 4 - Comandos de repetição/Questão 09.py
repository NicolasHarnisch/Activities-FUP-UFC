# Questão 09
# Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).

# Solução do exercício

def funcao(n):
    soma = 0
    numero = 0
    contador = 0
    while contador < n:
        soma += numero
        numero += 2
        contador += 1
    return soma