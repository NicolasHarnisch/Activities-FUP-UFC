# Questão 01
# Escreva um programa que:
# ◦ Crie/abra um arquivo texto de nome “arq.txt”
# ◦ Permita que o usuário grave diversas linhas nesse arquivo, até que o usuário entre com a linha ‘0’
# ◦ Feche o arquivo
# Agora, abra e leia o arquivo, e escreva na tela o conteúdo do arquivo.

# Solução do exercício

with open('arq.txt', 'w') as arquivo:
    while True:
        linha = input()
        if linha == '0':
            break
        arquivo.write(linha + '\n')
    arquivo.close()
    
with open('arq.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()