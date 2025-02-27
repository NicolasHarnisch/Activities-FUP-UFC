# Questão 21
# Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a saída para n = 6 seria:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# Solução do exercício

def funcao(n):
    for i in range(1, n + 1):
        espacos = n - i
        asteriscos = 2 * i - 1
        print(' ' * espacos + '*' * asteriscos)
