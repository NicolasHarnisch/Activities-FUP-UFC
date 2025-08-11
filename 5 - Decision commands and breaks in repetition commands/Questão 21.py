# Questão 21
# Faça uma função que receba dois números e retorne qual deles é o maior.

# Solução do exercício

def funcao(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2

# Pra rodar o Programa
x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1, x2)
print(f"{y:.2f}")