# Questão 19
# Faça uma função que receba dois vetores de mesmo tamanho e calcule outro vetor contendo, 
# nas posições pares o valores do primeiro vetor e nas posições ímpares os valores do segundo vetor.

# Solução do exercício

def funcao(x1, x2):
    x3 = []
    for i in range(len(x1)):
        x3.append(x1[i])
        x3.append(x2[i])
    return x3

# Pra rodar o programa
x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)