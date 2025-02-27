# Questão 12
# Escreva uma função que receba n e k tais que n ≥ k ≥ 0 e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)

# Solução do exercício

def funcao(n, k):
    z = 1
    t = 1
    y = n - k
    uru = 1
    for i in range(1, n+1):
        z *= i
    for i in range(1, k+1):
        t *= i
    
    for i in range (1, y+1):
        uru *= i
    
    c = z/(t*uru)
    return c

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")