# Questão 11
# Faça um programa para ler a nota de 15 alunos e armazene em um vetor, calcule e imprima a média geral.

# Solução do exercício

notas = []
for i in range(15):
    notas.append(float(input()))
soma = 0
for nota in notas:
    soma += nota
media = soma / 15
print(f"{media:.2f}")
