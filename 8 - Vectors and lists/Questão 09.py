# Questão 09
# Faça um programa que receba do usuário um vetor com 10 inteiros. Em seguida deverá ser mostrado na tela o maior e o menor valor desse vetor.

# Solução do exercício

vetor = []

for i in range(10):
    numero = int(input())
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for valor in vetor:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(maior)
print(menor)
