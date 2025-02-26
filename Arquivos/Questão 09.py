# Questão 09
# Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo). 
# O nome do terceiro arquivo deve ser o nome do primeiro arquivo seguido do nome do segundo arquivo. Mostre na tela o conteúdo do terceiro arquivo.

# Solução do exercício

arq1 = input()
arq2 = input()
arq3 = arq1 + arq2
with open(arq1, 'r') as arquivo:
    for linha in arquivo:
        with open(arq3, 'a') as arquivo3:
            arquivo3.write(linha)
            arquivo3.close()
    arquivo.close()

with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        with open(arq3, 'a') as arquivo3:
            arquivo3.write(linha)
            arquivo3.close()
    arquivo.close()

with open(arq3, 'r') as arquivo3:
    for linha in arquivo3:
        print(linha, end = '')
    arquivo3.close()
