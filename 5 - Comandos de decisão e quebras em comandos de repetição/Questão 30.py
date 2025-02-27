# Questão 30
# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. 
# A quantidade de números a serem lidos deve ser fornecida pelo usuário.

# Solução do exercício

n = int(input())
contador = 0
maior = None
quantidade = 0

while contador < n:
    numero = int(input())
    if maior is None or numero > maior:
        maior = numero
        quantidade = 1
    elif numero == maior:
        quantidade += 1
    contador += 1

print(maior)
print(quantidade)
