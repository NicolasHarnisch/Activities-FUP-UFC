# Questão 19
# Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).
# !
# !!
# !!!
# !!!!
# !!!!!
# Solução do exercício

def funcao(n):
    for i in range(1, n + 1):
        print('!' * i)

# Pra rodar o programa
x = int(input(""))
funcao(x)