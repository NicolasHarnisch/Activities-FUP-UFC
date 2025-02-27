# Questão 10
# Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).

# Solução do exercício

def funcao(x1, x2):
    if x1 > x2:
        for i in range(1, x1+1):
            if x1%i == 0 and x2%i == 0:
                resultado = i
    elif x2 >= x1:
        for i in range(1, x2+1):
            if x1%i == 0 and x2%i == 0:
                resultado = i
    return resultado

# Pra rodar o programa
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")