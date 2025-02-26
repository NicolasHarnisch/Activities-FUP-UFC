# Questão 05
# Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.

# Solução do exercício

arq = input()
caractere = input()
contador = 0

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            if letra == caractere:
                contador += 1
    arquivo.close()

print(contador)