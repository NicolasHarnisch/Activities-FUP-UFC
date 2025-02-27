# Questão 16
# Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os elementos que não aparecem repetidos.

# Solução do exercício

def funcao(x):
    unicos = []
    
    for i in range(len(x)):  
        repetido = False
        for j in range(len(x)):  
            if i != j and x[i] == x[j]:  
                repetido = True
                break  
        if not repetido:  
            unicos.append(x[i])  
    
    return unicos

# Pra rodar o programa
x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)