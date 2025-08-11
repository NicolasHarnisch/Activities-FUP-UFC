# Questão 22
# Faça um programa que preencha um vetor de tamanho 100, com os 100 primeiros naturais que não são múltiplos de 7 ou que terminam com 7.

# Solução do exercício

vetor = []
n = 1
while len(vetor) < 100:
    if n % 7 != 0 and n % 10 != 7:
        vetor.append(n)
    n += 1
print(vetor)
