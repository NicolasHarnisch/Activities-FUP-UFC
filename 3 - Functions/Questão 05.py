# Questão 05
# Faça uma função que, dado o tamanho do lado de um quadrado e retorne a sua área.

# Solução do exercício

def funcao(x):
    area = x ** 2
    return area

# Pra rodar o Programa
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")