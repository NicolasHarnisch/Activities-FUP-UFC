# Questão 05
# Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

# Solução do exercício

vetor = []

for i in range(10):
    numero = float(input())
    vetor.append(numero)

vetor_quadrado = []
for i in range(10):
    quadrado = vetor[i] * vetor[i]
    vetor_quadrado.append(quadrado)

for valor in vetor:
    print(f"{valor:.2f}")

for valor in vetor_quadrado:
    print(f"{valor:.2f}")
