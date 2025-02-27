# Questão 07
# Leia um vetor com 15 posições. Contar e escrever os valores pares desse vetor.

# Solução do exercício

vetor = []

for i in range(15):
    numero = int(input())
    vetor.append(numero)

par = []

for valor in vetor:
    if valor % 2 == 0:
        par.append(valor)

print(len(par))

for p in par:
    print(p)
