# Questão 31
# Digite um nome e imprima quantas letras diferentes tem esse nome.

# Solução do exercício

def contar_letras(nome):
    return len(set(letra for letra in nome if letra.isalpha()))

nome = input()
print(contar_letras(nome))
