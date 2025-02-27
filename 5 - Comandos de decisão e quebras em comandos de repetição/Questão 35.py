# Questão 35
# O numero 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e 552 = 3025. Elaborar um algoritmo que verifique todos os números de quatro algarismos que apresentem essa propriedade. Não use operações com strings.

# Solução do exercício

for numero in range(1000, 10000):
    numero1 = numero // 100
    numero2 = numero % 100
    if (numero1 + numero2) ** 2 == numero:
        print(numero)
