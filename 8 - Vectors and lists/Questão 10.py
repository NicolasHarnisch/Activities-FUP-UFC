# Questão 10
# Leia um vetor de 20 inteiros e atribua 0 para todos os elementos que possuírem valores negativos.

# Solução do exercício

vetor = []
for i in range(20):
    vetor.append(int(input()))
for i in range(20):
    if vetor[i] < 0:
        vetor[i] = 0
for valor in vetor:
    print(valor)
