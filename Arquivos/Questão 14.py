# Questão 14
# Dado um arquivo contendo um conjunto de nomes e datas de nascimento (DD MM AAAA, isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data de hoje e construa outro arquivo 
# contendo o nome e a idade de cada pessoa do primeiro arquivo. No arquivo de entrada, o nome está separado da data de nascimento por uma tabulação, mas as informações da data de nascimento estão separadas por um espaço em branco. 
# A data de hoje da entrada será dada em três inteiros diferentes, dia, mês e ano. O arquivo de saída deve ter o mesmo nome do arquivo de entrada, mas terminando em .out (por exemplo, se a entrada for arquivo.txt, a saída deve ser arquivo.txt.out). 
# Escreva na tela o conteúdo desse arquivo.

# Solução do exercício

arq = input()
diaatual = int(input())
mesatual = int(input())
anoatual = int(input())

def calcular_idade(d, m, a):
    d = int(d)
    m = int(m)
    a = int(a)
    idade = anoatual - a
    if (mesatual, diaatual) < (m, d):
        idade -= 1
    return idade
    
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        nome, data = linha.split('\t')
        d, m, a = data.split()
        idade = calcular_idade(d, m, a)
        with open(f'{arq}.out', 'a') as arquivo2:
            linha2 = f'{nome}\t{idade}\n'
            arquivo2.write(linha2)
            
with open(f'{arq}.out', 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
