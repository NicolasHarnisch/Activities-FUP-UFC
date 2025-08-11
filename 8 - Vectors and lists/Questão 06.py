# Questão 06
# Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondente a duas posições no vetor. 
# Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

# Solução do exercício

vetor = []

for j in range(8):
    numero = float(input())
    vetor.append(numero)

X = int(input())
Y = int(input())

valores = vetor[X] + vetor[Y]

print(f"{valores:.2f}")
