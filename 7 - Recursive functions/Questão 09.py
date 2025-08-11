# Questão 09
# Faça uma função recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. Exemplo de superfatorial: sf (4) = 1! * 2! * 3! * 4! = 288.

# Solução do exercício

def sf(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fatorial(x) * sf(x - 1)

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

# Pra rodar o Programa
x = int(input(""))
y = sf(x)
print(f"{y}")