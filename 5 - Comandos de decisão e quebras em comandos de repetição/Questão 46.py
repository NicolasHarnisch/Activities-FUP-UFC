# Questão 46
# Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. 
# Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. 
# Exemplos:
# ovo
# arara
# Socorram-me, subi no onibus em Marrocos.
# Anotaram a data da maratona

# Solução do exercício

entrada = input("")
texto_limpo = ""

for caractere in entrada:
    if "a" <= caractere.lower() <= "z":
        texto_limpo += caractere.lower()

inicio = 0
fim = len(texto_limpo) - 1

while inicio < fim:
    if texto_limpo[inicio] != texto_limpo[fim]:
        print(False)
        break
    inicio += 1
    fim -= 1
else:
    print(True)
