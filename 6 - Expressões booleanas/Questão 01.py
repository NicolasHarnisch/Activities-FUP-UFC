# Questão 01
# Entre com um nome e imprima o nome somente se a primeira letra do nome for “a” (maiúscula ou minúscula).

# Solução do exercício

def imprimir():
    nome = input('')
    if nome[0] == 'a' or nome[0] == 'A':
        print(nome)

imprimir()