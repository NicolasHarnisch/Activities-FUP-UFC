# Quesão 08
# Faça um programa que leia o conteúdo de um arquivo e crie outro arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. 
# Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. Escreva na tela o conteúdo dos dois arquivos, primeiro o do arquivo de entrada e depois o do arquivo de saída.

# Solução do exercício

arq = input()
arq2 = input()

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            with open(arq2, 'a') as arquivo2:
                arquivo2.write(letra.upper())
                arquivo2.close()
    arquivo.close()

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()
with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()