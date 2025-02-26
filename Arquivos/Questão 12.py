# Questão 12

# Abra um arquivo texto, calcule e escreva na tela o número de caracteres, o número de linhas e o número de palavras neste arquivo. 
# Também escreva na tela quantas vezes cada letra ocorre no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.

# Solução do exercício

letras = 'abcdefghijklmnopqrstuvwxyz'
contletras = [0]*26
arq = input()
contlinhas = 0
contcaracteres = 0
contpalavras = 0

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        contlinhas += 1
        palavras = linha.split()
        contpalavras += len(palavras)
        for char in linha:
            contcaracteres += 1
            pos = 0
            for l in letras:
                if char.lower() == l:
                    contletras[pos] += 1
                    break
                pos += 1

print(contcaracteres)
print(contlinhas)
print(contpalavras)
for i in range(26):
    print(f'{letras[i]}: {contletras[i]}')
