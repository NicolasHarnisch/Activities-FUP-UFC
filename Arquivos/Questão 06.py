# Questão 06
# Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo. ]
# Letras maiúsculas e minúsculas devem ser contadas juntas, e não separadamente.

# Solução do exercício

letras = 'abcdefghijklmnopqrstuvwxyz'
contletras = [0] * 26 
arq = input()

with open(arq, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        for letra in linha:
            letra = letra.lower() 
            for i in range(26):  
                if letra == letras[i]:
                    contletras[i] += 1
                    break  

for i in range(26):  
    print(f'{letras[i]}: {contletras[i]}')
