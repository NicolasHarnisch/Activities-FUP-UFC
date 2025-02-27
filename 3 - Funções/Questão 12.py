# Questão 12

# Faça uma função que receba o salário de um funcionário e calcule o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.

# Solução do exercício

def funcao(x):
    novo_salario = x * (1 + 21.37 / 100)
    return novo_salario