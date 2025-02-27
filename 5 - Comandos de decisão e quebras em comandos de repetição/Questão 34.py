# Questão 34
# Escreva um programa que gera todos os números entre 1000 − 1999 e mostra aqueles que divididos por 11 dão resto 5.

# Solução do exercício

for i in range(1000, 2000):
    if i % 11 == 5:
        print(i)
