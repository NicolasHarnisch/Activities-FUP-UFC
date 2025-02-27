# Questão 25
# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

# Solução do exercício

soma = 0
contador = 0

while contador < 10:
    numero = int(input())
    if numero > 0:
        soma += numero
        contador += 1

media = soma / contador
print(f"{media:.2f}")
