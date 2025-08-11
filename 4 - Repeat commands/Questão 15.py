# Questão 15
# Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! . . . 1/n!.


# Solução do exercício

def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def funcao(n):
    e = 1
    for i in range(1, n + 1):
        e += 1 / fatorial(i)
    return e

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y:.8f}")