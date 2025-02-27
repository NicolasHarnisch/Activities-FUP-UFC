# Questão 16
# Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas, minutos e segundos.

# Solução do exercício

def funcao(x):
    horas = x // 3600
    minutos = (x % 3600) // 60
    segundos_restantes = x % 60
    
    return horas, minutos, segundos_restantes

#pra rodar o programa
x = int(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")