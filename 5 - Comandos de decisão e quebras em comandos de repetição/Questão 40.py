# Quesão 40
# Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.

# Solução do exercício

def contarCaractere(string):
    contador = 0
    for caractere in string:
        if caractere == '1':
            contador += 1
    return contador

string = input("")

resultado = contarCaractere(string)
print(f"{resultado}")
