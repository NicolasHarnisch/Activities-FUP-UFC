# Questão 03
# Faça um programa que receba uma palavra e um caractere (vogal ou consoante) e imprima quantas vogais (a, e, i, o, u) possui essa palavra. 
# Substitua todas as vogais da palavra dada pelo caractere dado, e imprima a nova palavra.

# Solução do exercício

stri = input()
vogais = 'AEIOUaeiou'
consoante = input()
frase = ''
contador = 0
for letra in stri:
    if letra not in vogais:
        frase += letra
    elif letra in vogais:
        frase += consoante
        contador += 1
print(contador)
print(frase)