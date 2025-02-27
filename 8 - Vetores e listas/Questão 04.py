# Questão 04
# Crie um programa que lê 10 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.

# Solução do exercício

valores = []

for i in range(10):
    numero = int(input())
    valores.append(numero)

for i in range(9, -1, -1):
    print(valores[i])