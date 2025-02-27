# Questão 03
# Construa um dicionário com as seguintes informações de alunos: nome, número de matrícula e curso. Leia do usuário a informação de n alunos, 
# armazene em um vetor e imprima os dados na tela.

# Solução do exercício

def main():
    alunos = []
    n = int(input())
    for _ in range(n):
        nome = input().strip()
        matricula = int(input().strip())
        curso = input().strip()
        aluno = {'nome': nome, 'matricula': matricula, 'curso': curso}
        alunos.append(aluno)
    for aluno in alunos:
        print(aluno)

if __name__ == "__main__":
    main()
