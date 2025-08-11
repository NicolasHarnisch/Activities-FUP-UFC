# Questão 04
# Escreva um trecho de código para fazer a criação dos novos tipos de dados conforme solicitado abaixo:
# ◦ Data: composto de dia, mês e ano.
# ◦ Horário: composto de hora, minutos e segundos.
# ◦ Compromisso: composto de uma data, horário e texto que descreve o compromisso.
# Leia n compromissos. Crie uma função que, dadas duas datas, retorne se a primeira ocorre antes da segunda ou não. Crie outra função semelhante, 
# mas para comparar horários. Mostre os compromissos em ordem de data e horário.

# Solução do exercício

def data():
    data = {}
    data['dia'] = int(input("Dia: "))
    data['mes'] = int(input("Mes: "))
    data['ano'] = int(input("Ano: "))
    return data

def horas():
    horario = {}
    horario['hora'] = int(input("Hora: "))
    horario['minuto'] = int(input("Minuto: "))
    horario['segundo'] = int(input("Segundo: "))
    return horario

def ordem(data_1, data_2):
    d1, h1 = data_1['data'], data_1['horario']
    d2, h2 = data_2['data'], data_2['horario']
    if (d1['ano'], d1['mes'], d1['dia'], h1['hora'], h1['minuto'], h1['segundo']) < (d2['ano'], d2['mes'], d2['dia'], h2['hora'], h2['minuto'], h2['segundo']):
        return True
    else:
        return False

x = int(input())

compromissos = []

for i in range(x):
    valor_certo = {}
    valor_certo['data'] = data()
    valor_certo['horario'] = horas()
    valor_certo['descricao'] = input("Descricao: ")
    compromissos.append(valor_certo)

for i in range(x):
    for j in range(x - i - 1):
        if ordem(compromissos[j], compromissos[j+1]) == False:
            compromissos[j], compromissos[j +
                                          1] = compromissos[j+1], compromissos[j]

for data in compromissos:
    print(data)