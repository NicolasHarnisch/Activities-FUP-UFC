# Questão 36
# Faça uma função que retorne o maior fator primo de um número.

# Solução do exercício

def funcao(n):
    fator = 2
    maior_fator = 1
    while fator * fator <= n:
        if n % fator == 0:
            maior_fator = fator
            while n % fator == 0:
                n //= fator
        fator += 1
    if n > 1:
        maior_fator = n
    return maior_fator

# Pra rodar o programa
x = int(input(""))
y = funcao(x)
print(f"{y}")