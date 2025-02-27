# Questão 18
# Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. 
# Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.

# Solução do exercício

def funcao(data):
    meses = [
        "janeiro", "fevereiro", "marco", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    dia = int(data[0] + data[1])
    mes = int(data[3] + data[4])
    ano = data[6] + data[7] + data[8] + data[9]
    
    return f"{dia} de {meses[mes - 1]} de {ano}"

#Pra rodar o programa
x = input("")
y = funcao(x)
print(f"{y}")