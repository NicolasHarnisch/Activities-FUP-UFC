# Questão 12
# Faça um programa que leia os dados de 10 alunos (Nome, matricula, Média Final), armazenando em um vetor. 
# Uma vez lidos os dados, divida estes dados em 2 novos vetores, o vetor dos aprovados e o vetor dos reprovados, 
# considerando a média mínima para a aprovação como sendo 5.0. Exibir na tela os dados do vetor de aprovados, seguido dos dados do vetor de reprovados.

# Solução do exercício

def ler_alunos(qtd):
    alunos = []
    for _ in range(qtd):
        nome = input()
        matricula = int(input())
        media = float(input())
        alunos.append({"nome": nome, "matricula": matricula, "media": media})
    return alunos

def separar_aprovados_reprovados(alunos):
    aprovados = []
    reprovados = []
    for aluno in alunos:
        if aluno["media"] >= 5.0:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)
    return aprovados, reprovados

def exibir_alunos(lista):
    for aluno in lista:
        print(aluno)

def main():
    alunos = ler_alunos(10)
    aprovados, reprovados = separar_aprovados_reprovados(alunos)
    exibir_alunos(aprovados)
    exibir_alunos(reprovados)

if __name__ == "__main__":
    main()
