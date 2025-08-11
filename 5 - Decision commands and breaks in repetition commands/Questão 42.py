# Questão 42
# Ler uma frase e contar quantos caracteres são brancos. Não use nenhuma funcionalidade do python que já faça isso.

# Solução do exercício

def contarEspacos(frase):
    contagem = 0
    for caractere in frase:
        if caractere == ' ':
            contagem += 1
    return contagem

frase = input("")

resultado = contarEspacos(frase)
print(f"{resultado}")
