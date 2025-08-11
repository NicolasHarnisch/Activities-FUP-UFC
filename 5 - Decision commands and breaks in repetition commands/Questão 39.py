# Questão 39
# Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. 
# Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.

# Solução do exercício

def comparacao(palavra1, palavra2):
    i = 0

    while True:
        if i < len(palavra1):
            if i < len(palavra2):
                if palavra1[i] < palavra2[i]:
                    return palavra1
                elif palavra1[i] > palavra2[i]:
                    return palavra2
                i += 1
            else:
                return palavra2
        else:
            return palavra1

palavra1 = input("")
palavra2 = input("")

resultado = comparacao(palavra1, palavra2)
print(f"{resultado}")
