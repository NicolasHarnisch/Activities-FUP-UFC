# Questão 04
# Faça uma função que, dado um número inteiro e retorne o seu antecessor e o seu sucessor.

# Solução do exercício

def funcao(x):
    antecessor = x - 1
    sucessor = x + 1
    return antecessor, sucessor

# Pra rodar o Programa
x = int(input(""))
y1,y2 = funcao(x)
print(f"{y1}")
print(f"{y2}")