# Questão 21
# Faça um vetor de tamanho 70 preenchido com o seguinte valor: (i + 5*i) % (i + 1) , sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.

# Solução do exercício

vetor = []
for i in range(70):
    vetor.append((i + 5 * i) % (i + 1))
print(vetor)
