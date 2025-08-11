# Questão 04
# Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.

# Solução do exercício

arq = input()
vogais ='aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
contador1 = 0
contador2 = 0

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            if letra in vogais:
                contador1 += 1
            elif letra in consoantes:
                contador2 += 1
    arquivo.close()
print(contador1)
print(contador2)