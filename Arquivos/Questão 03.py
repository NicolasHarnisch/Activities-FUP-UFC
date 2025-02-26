# Questão 03
# Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais.

# Solução do exercício

def contar_vogais(arq):
    contador = 0
    with open(arq, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            for c in linha:
                if c in "aeiouAEIOU":
                    contador += 1
    return contador

print(contar_vogais(input()))