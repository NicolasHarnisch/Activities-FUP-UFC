# Quesão 08
# Escreva uma função recursiva SomaSerie(i,j,k). Esta função devolve a soma da série de valores no intervalo [i,j], com incremento k.

# Solução do exercício

def SomaSerie(x1, x2, x3):
    if x1 > x2:
        return 0
    else:
        return x1 + SomaSerie(x1 + x3, x2, x3)

# Pra rodar o Programa
x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
y = SomaSerie(x1, x2, x3)
print(f"{y}")