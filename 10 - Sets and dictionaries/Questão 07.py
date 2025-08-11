# Questão 07
# Faça um programa que realize a leitura dos seguintes dados relativos a um conjunto de alunos: Matricula, Nome, Código da Disciplina, Nota1 e Nota2.
# O tamanho da turma deve ser dado pelo usuário. Após ler todos os dados digitados, e depois de armazená-los em um vetor de dicionários, 
# exiba na tela a listagem final dos alunos com as suas respectivas médias finais (use uma média ponderada: Nota1 com peso=1.0 e Nota2 com peso=2.0). 
# Para cada aluno, inclua a média no dicionário.

# Solução do exercício

def calcular(nota1, nota2):
    return (nota1 * 1 + nota2 * 2) / 3 


def main():
    turma = []

    n = int(input())

    for _ in range(n):
        matricula = int(input())
        nome = input()
        codigo = input()
        nota1 = float(input())
        nota2 = float(input())

        media = calcular(nota1, nota2)

        aluno = {
            'matricula': matricula,
            'nome': nome,
            'codigo': codigo,
            'nota1': nota1,
            'nota2': nota2,
            'media': media
        }

        turma.append(aluno)

    for aluno in turma:
        print(aluno)


if __name__ == "__main__":
    main()
