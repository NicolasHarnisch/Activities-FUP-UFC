# Questão 28
# Faça um programa para ler 12 inteiros DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados na ordem que forem sendo lidos, 
# mas caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Exibir na tela o vetor final que foi digitado.

# Solução do exercício

numeros = []

while len(numeros) < 12:
    num = int(input())
    if num in numeros:
        print(f"Numero {num} ja existe, escreva outro")
    else:
        numeros.append(num)

print(numeros)
