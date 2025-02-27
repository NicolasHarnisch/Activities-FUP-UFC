# Questão 18
# Faça uma função que receba dois vetores, A e B, de mesmo tamanho. Crie um novo vetor denominado C calculando C = A – B (a diferença elemento a elemento). Retorne o vetor C.

# Solução do exercício

def funcao(x1, x2):
    x3 = []
    
    for i in range(len(x1)):  
        x3.append(x1[i] - x2[i])  
    
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