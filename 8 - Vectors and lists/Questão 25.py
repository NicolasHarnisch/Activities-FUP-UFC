# Questão 25
# Faça uma função que receba dois vetores. Retorne um vetor que seja a união entre os 2 vetores anteriores, ou seja, 
# que contém os números que estão em qualquer um dos vetores. Esse vetor de retorno não deve conter números repetidos.


# Solução do exercício

def funcao(x1, x2):
    resultado = []

    for num in x1:
        if num not in resultado:
            resultado.append(num)

    for num in x2:
        if num not in resultado:
            resultado.append(num)

    return resultado

# Pra rodar o programa
x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)
