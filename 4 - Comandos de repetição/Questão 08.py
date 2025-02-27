# Quesão 08
# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

# Solução do exercício

def imprimir_impares(n):
    contador = 0
    numero = 1
    while contador < n:
        print(numero)
        numero += 2
        contador += 1

n = int(input())
imprimir_impares(n)
