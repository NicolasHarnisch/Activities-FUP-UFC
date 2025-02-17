# Questão 04
# Escreva um programa que recebe uma string S e inteiros não-negativos I e J e imprima o segmento S[I...J].

# Solução do exercício

S = input().strip()
I = int(input())
J = int(input())

print(S[I-1:J])
