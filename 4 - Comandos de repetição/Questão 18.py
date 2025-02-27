# Questão 18
# Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . 
# Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.

# Solução do exercício

def fatorial(p):
    f = 1
    for i in range(1, p + 1):
        f *= i
    return f

def funcao(p):
    fatorial_p = fatorial(p)
    soma = sum(int(digito) for digito in str(fatorial_p))
    return soma

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y}")