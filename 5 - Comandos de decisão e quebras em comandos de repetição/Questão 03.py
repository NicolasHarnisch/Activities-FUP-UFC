# Questão 03
# Ler 4 números inteiros e calcular a soma dos que forem par.

# Solução do exercício

def soma_pares():
    soma = 0
    for i in range(4):
        n = int(input())
        if n % 2 == 0:
            soma += n
    print(soma)

soma_pares()
