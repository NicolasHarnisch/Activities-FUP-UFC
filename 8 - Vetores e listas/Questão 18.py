# Questão 18
# Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor 
# serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

# Solução do exercício

valor_saque = int(input())

notas_100 = valor_saque // 100
valor_saque %= 100

notas_50 = valor_saque // 50
valor_saque %= 50

notas_20 = valor_saque // 20
valor_saque %= 20

notas_10 = valor_saque // 10
valor_saque %= 10

notas_5 = valor_saque // 5
valor_saque %= 5

notas_2 = valor_saque // 2
valor_saque %= 2

notas_1 = valor_saque // 1

print(f"{notas_100}")
print(f"{notas_50}")
print(f"{notas_20}")
print(f"{notas_10}")
print(f"{notas_5}")
print(f"{notas_2}")
print(f"{notas_1}")
