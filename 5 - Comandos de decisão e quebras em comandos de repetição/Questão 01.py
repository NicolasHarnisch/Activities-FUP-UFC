# Questão 01
# Faça um programa que receba dois números inteiros e imprima o maior deles, se por acaso os dois números forem iguais, imprima a mensagem “Numeros iguais”.


# Solução do exercício

def maior_numero():
    a = int(input())
    b = int(input())
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Numeros iguais")

maior_numero()
