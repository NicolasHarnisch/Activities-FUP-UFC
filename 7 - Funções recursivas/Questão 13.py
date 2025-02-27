# Questão 13
# Implemente a função A definida recursivamente por: A(m, n) = n + 1, se m = 0; A(m, n) = A(m − 1, 1), se m > 0 e n = 0; A(m, n) = A(m − 1, A(m, n − 1)) , se m > 0 e n > 0.

# Solução do exercício

def A(x1, x2):
    if x1 == 0:
        return x2 + 1
    elif x1 > 0 and x2 == 0:
        return A(x1 - 1, 1)
    else:  
        return A(x1 - 1, A(x1, x2 - 1))

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = A(x1, x2)
print(f"{y}")