# Questão 12
# Implemente a função h definida recursivamente por: h(m, n) = m + 1, se n = 1; h(m, n) = n + 1, se m = 1, h(m, n) = h(m, n − 1) + h(m − 1, n), se m > 1, n > 1.

# Solução do exercício

def h(x1, x2):
    if x2 == 1:
        return x1 + 1
    elif x1 == 1:
        return x2 + 1
    else:
        return h(x1, x2 - 1) + h(x1 - 1, x2)

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = h(x1, x2)
print(f"{y}")