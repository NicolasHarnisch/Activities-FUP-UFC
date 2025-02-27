# Questão 02
# Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.

# Solução do exercício

def imprimir():
    string = input()
    resultado = ""
    for letra in string:
        if letra not in 'aeiouAEIOU':
            resultado += letra
    print(resultado)

imprimir()
