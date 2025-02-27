# Questão 11
# Faça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. Nessa função, 
# verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos. Caso alguma verificação não seja válida, os retornos devem ser iguais a zero.

# Solução do exercício

def funcao(data):
    if len(data) == 10 and data[2] == '/' and data[5] == '/':
        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:10]
        
        if dia[0] >= '0' and dia[0] <= '9' and dia[1] >= '0' and dia[1] <= '9' and \
           mes[0] >= '0' and mes[0] <= '9' and mes[1] >= '0' and mes[1] <= '9' and \
           ano[0] >= '0' and ano[0] <= '9' and ano[1] >= '0' and ano[1] <= '9' and \
           ano[2] >= '0' and ano[2] <= '9' and ano[3] >= '0' and ano[3] <= '9':
            return int(dia), int(mes), int(ano)
    
    return 0, 0, 0