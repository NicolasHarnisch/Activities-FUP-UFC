# Questão 09
# Ler três valores e imprimi-los na tela em ordem crescente.

# Solução do exercício

def ordenar_valores(valor1, valor2, valor3):
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    if valor1 > valor3:
        valor1, valor3 = valor3, valor1
    if valor2 > valor3:
        valor2, valor3 = valor3, valor2
    print(int(valor1))
    print(int(valor2))
    print(int(valor3))

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

ordenar_valores(valor1, valor2, valor3)
