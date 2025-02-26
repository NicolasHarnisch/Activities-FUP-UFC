# Questão 02
# Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui.

# Solução do exercício

contador = 0
arq = input()
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        contador += 1
    arquivo.close()
print(contador)