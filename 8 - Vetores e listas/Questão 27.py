# Questão 27
# Faça uma função que receba um vetor posições e o compacte, ou seja, elimine as posições com valor zero. 
# Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. No final, retorne o vetor compacto.

# Solução do exercício

def funcao(vetor):
    x = []
    
    for num in vetor:
        if num != 0:
            x.append(num)

    return x

# Pra rodar o programa
x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)