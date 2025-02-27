# Questão 10
# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

# Solução do exercício

def dia_da_semana(numero):
    if numero == 1:
        print("Domingo")
    elif numero == 2:
        print("Segunda-feira")
    elif numero == 3:
        print("Terca-feira")
    elif numero == 4:
        print("Quarta-feira")
    elif numero == 5:
        print("Quinta-feira")
    elif numero == 6:
        print("Sexta-feira")
    elif numero == 7:
        print("Sabado")

numero = int(input())
dia_da_semana(numero)
