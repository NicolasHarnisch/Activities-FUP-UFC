# Questão 19
# Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias 
# para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

# Solução do exercício

def funcao(x):
    notas_100 = x // 100
    x = x % 100
    notas_50 = x // 50
    x = x % 50
    notas_20 = x // 20
    x = x % 20
    notas_10 = x // 10
    x = x % 10
    notas_5 = x // 5
    x = x % 5
    notas_2 = x // 2
    x = x % 2
    notas_1 = x // 1
    
    return notas_100, notas_50, notas_20, notas_10, notas_5, notas_2, notas_1
