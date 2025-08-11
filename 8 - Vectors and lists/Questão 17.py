# Questão 17
# Faça uma função que receba um vetor e um número inteiro x e retorne os múltiplos do número x que existem no vetor.

# Solução do exercício

def funcao(x1, x2):
    resultado = []
    
    for i in range(len(x1)):  
        if x1[i] % x2 == 0:  
            resultado.append(x1[i])  
    
    return resultado

# Pra rodar o programa
x1 = []
for i in range(10):
    x1.append(int(input("")))
x2 = int(input(""))
y = funcao(x1, x2)
print(y)