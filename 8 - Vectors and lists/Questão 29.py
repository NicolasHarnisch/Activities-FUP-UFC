# Questão 29
# Faça uma função que, dado um vetor de números reais, ordene os elementos desse vetor do maior para o menor, e retorne o vetor ordenado. 
# Não use nenhuma função de ordenação do python.

# Solução do exercício

def funcao(x):
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] < x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

# Pra rodar o programa
x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)