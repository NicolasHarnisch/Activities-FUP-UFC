# Questão 15
# Continuando o programa da questão anterior, escreva no arquivo de saída, além da idade, uma string que representa a sua maioridade:
# ◦ Se a idade for menor do que 18 anos, escreva “menor de idade”
# ◦ Se a idade for maior do que 18 anos, escreva “maior de idade”
# ◦ Se a idade for igual a 18 anos, escreva “entrando na maioridade”

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

with open(arq, 'r') as arquivo, open(f'{arq}.out', 'w') as arquivo2:
    for linha in arquivo:
        nome, data = linha.strip().split('\t')
        d, m, a = data.split()
        idade = calcular_idade(d, m, a)
        if idade > 18:
            linha2 = f"{nome}\t{idade}\tmaior de idade\n"
        elif idade == 18:
            linha2 = f"{nome}\t{idade}\tentrando na maioridade\n"
        else:
            linha2 = f"{nome}\t{idade}\tmenor de idade\n"
        arquivo2.write(linha2)

with open(f"{arq}.out", "r") as arquivo:
    for linha in arquivo:
        print(linha, end="")
