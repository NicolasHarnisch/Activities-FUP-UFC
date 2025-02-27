# Questão 02
# Faça um programa que receba um número inteiro e imprima se o número é par ou ímpar.

# Solução do exercício

def par_ou_impar():
    n = int(input())
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")

par_ou_impar()
