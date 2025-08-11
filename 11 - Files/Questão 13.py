# Questão 13
# Faça um programa que leia um arquivo com diversos nomes e telefones cadastrados, um por linha, e separados por uma tabulação. 
# Guarde essas informações em uma lista de dicionários. Imprima esses dicionários na tela, ordenados pelo nome. O nome do arquivo é dado como entrada para o programa.

# Solução do exercício

arq = input()
pessoas = []
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        pessoa = {}
        nome, telefone = linha.split('\t')
        pessoa['nome'] = nome
        pessoa['telefone'] = telefone.replace('\n', '')
        pessoas.append(pessoa)
    arquivo.close()

for i in range(len(pessoas)):
    for j in range(len(pessoas)):
        if pessoas[i]['nome'] < pessoas[j]['nome']:
            pessoas[i], pessoas[j] = pessoas[j], pessoas[i]
for pessoa in pessoas:
    print(pessoa)