# Questão 32
# Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

# Solução do exercício

palavra = input()
resultado = ""

for char in palavra:
    resultado += chr(ord(char) + 1)

print(resultado)