# Questão 41
# Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.

# Solução do exercício

def substituir_zeros(valor):
    resultado = ""
    for i in valor:
        if i == "0":  
            resultado += "1"
        else:
            resultado += i  
    return resultado

valor = input()

resultado = substituir_zeros(valor)
print(resultado)
