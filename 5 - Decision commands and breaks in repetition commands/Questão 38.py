# Questão 38
# Crie uma função que diga se duas strings são iguais ou não, analisando caractere a caractere.

# Solução do exercício

def funcao(x, y):
    i = 0

    while True:
        if i < len(x):
            if i < len(y):
                if x[i] != y[i]:
                    return False
                i += 1
            else:
                break
        else:
            break

    if i == len(x):
        if i == len(y):
            return True

    return False

# Pra rodar o programa
x1 = input("")
x2 = input("")
y = funcao(x1, x2)
print(f"{y}")