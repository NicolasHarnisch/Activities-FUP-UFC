# Questão 01
# Faça um função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso. 
# Exemplo: Data: 01/01/2000 , imprimir: 1 de janeiro de 2000.

# Solução do exercício

def funcao(data):
    partes = data.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    return str(dia) + " de " + meses[mes - 1] + " de " + str(ano)

# Pra rpodar o programa
x = input("")
y = funcao(x)
print(f"{y}")