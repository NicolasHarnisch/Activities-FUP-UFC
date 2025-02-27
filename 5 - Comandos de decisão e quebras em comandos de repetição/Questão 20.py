# Questão 20
# Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9...

# Solução do exercício

import math

def funcao(numero):
    if numero < 0:
        return False
    raiz = math.sqrt(numero)
    return raiz == int(raiz)

# Pra rodar o Programa
x = float(input(""))
y = funcao(x)
print(f"{y}")