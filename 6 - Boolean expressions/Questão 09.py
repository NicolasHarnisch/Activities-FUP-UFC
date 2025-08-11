# Questão 09
# Faça uma função que receba 2 números inteiros positivos e calcule o Mínimo Múltiplo Comum (MMC).

# Solução do exercício

def funcao(a, b):
    maior = max(a, b)
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1

# Pra rodar o Programa
x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")