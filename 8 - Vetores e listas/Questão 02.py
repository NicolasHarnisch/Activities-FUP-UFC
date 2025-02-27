# Questão 02
# Faça um programa que possua um vetor denominado A que armazena 6 números inteiros. O programa deve executar os seguintes passos:
# ◦ Atribua os seguintes valores a esse vetor: 1, 0, 5, −2, −5, 7 .
# ◦ Armazena em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1], A[5] do vetor e mostre na tela esta soma.
# ◦ Modifique o vetor na posição 3, atribuindo a esta posição o valor -89.
# ◦ Mostre na tela cada valor do vetor A, em cada linha.

# Solução do exercício

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(soma)

A[3] = -89

for valor in A:
    print(valor)
