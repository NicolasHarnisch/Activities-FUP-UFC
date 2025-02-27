# Questão 06
# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# ◦ Ter pelo menos 65 anos;
# ◦ Ou ter trabalhado pelo menos 30 anos;
# ◦ Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
# Solução do exercício

def aposentadoria():
    idade = int(input())
    trabalho = int(input())
    
    if idade >= 65 or trabalho >= 30 or (idade >= 60 and trabalho >= 25):
        print("Pode se aposentar")
    else:
        print("Nao pode se aposentar")

aposentadoria()
