# Questão 11
# Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.

# Solução do exercício

def funcao(n):
    fatorial = 1
    contador = 1
    while contador <= n:
        fatorial *= contador
        contador += 1
    return fatorial

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y}")