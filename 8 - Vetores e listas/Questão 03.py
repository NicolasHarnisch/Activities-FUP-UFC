# Questão 03
# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

# Solução do exercício

valores = []

for i in range(6):
    numero = int(input())
    valores.append(numero)

for valor in valores:
    print(valor)
