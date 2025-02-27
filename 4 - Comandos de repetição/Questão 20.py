# Questão 20
# Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. Por exemplo, a saída para n = 4 seria:
# *
# **
# ***
# ****
# ***
# **
# *
# Solução do exercício

def funcao(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Pra rodar o programa
x = int(input(""))
funcao(x)