# Quesão 08
# Leia um vetor com 15 posições. Somar e mostrar os números que são ímpares.

# Solução do exercício

vetor = []

for i in range(15):
    numero = int(input())
    vetor.append(numero)

impar = []
soma_impar = 0

for valor in vetor:
    if valor % 2 != 0:
        impar.append(valor)
        soma_impar += valor

print(soma_impar)

for num in impar:
    print(num)
