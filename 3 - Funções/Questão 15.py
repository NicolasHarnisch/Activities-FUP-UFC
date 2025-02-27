# Questão 15
# Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.

# Solução do exercício

segundos_totais = int(input())

horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(horas)
print(minutos)
print(segundos)
