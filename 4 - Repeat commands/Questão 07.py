# Questão 07
# Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido.

# Solução do exercício

def funcao(N):
    soma = 0
    for i in range(1, N + 1):
        soma += i
    return soma

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y}")