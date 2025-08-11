# Questão 07
# Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’. 
# Esse arquivo de saída deve ter o mesmo nome do arquivo de entrada, mas terminando em .out (por exemplo, se a entrada for arquivo.txt, a saída deve ser arquivo.txt.out). 
# Escreva na tela o conteúdo desse arquivo.

# Solução do exercício

arq = input()
vogais = 'AEIOUaeiou'
with open(arq, 'r') as arquivo:
    arq2 = f'{arq}.out'
    for linha in arquivo:
        for letra in linha:
            with open(arq2, 'a') as arquivo2:
                if letra in vogais:
                    arquivo2.write("*")
                else:
                    arquivo2.write(letra)
                arquivo2.close()
arquivo.close()

with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()