# Questão 13
# O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
# ◦ F1 = 1
# ◦ F2 = 1
# ◦ Fn = Fn−1 + Fn−2 para n> 2
# Faça uma função que receba um valor inteiro n e calcule e Fn.
# Solução do exercício

def funcao(n):
    a, b = 1, 1
    contador = 2
    while contador < n:
        a, b = b, a + b
        contador += 1
    return b if n > 1 else a

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y}")