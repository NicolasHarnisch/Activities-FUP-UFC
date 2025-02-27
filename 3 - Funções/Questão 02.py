# Questão 02
# Crie uma função que permita fazer a conversão cambial de Dólares para Reais. Considere como taxa de câmbio US$ 1,0 = R$5,27.

# Solução do exercício

def funcao(x):
    return x*5.27

# Pra rodar o Programa
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")