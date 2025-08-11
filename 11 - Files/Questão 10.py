# Questão 10
# Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada linha o nome de uma cidade e o seu número de habitantes, separados por uma tabulação. 
# O programa deverá ler o arquivo de entrada, armazenar os dados das cidades em uma lista de dicionários, e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes. 
# Mostre na tela lista dos dicionários e o conteúdo desse arquivo de saída.

# Solução do exercício

arq = input()
cidades = []
maiorcidade = None

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        nome_cidade, habitantes = linha.strip().split('\t')
        habitantes = int(habitantes)
        cidades.append({'nome': nome_cidade, 'habitantes': habitantes})
        if maiorcidade is None or habitantes > maiorcidade['habitantes']:
            maiorcidade = {'nome': nome_cidade, 'habitantes': habitantes}

with open(f'{arq}.out', 'w') as arquivo:
    arquivo.write(f"{maiorcidade['nome']}\t{maiorcidade['habitantes']}\n")

for cidade in cidades:
    print(cidade)

with open(f'{arq}.out', 'r') as arquivo:
    print(arquivo.read().strip())
