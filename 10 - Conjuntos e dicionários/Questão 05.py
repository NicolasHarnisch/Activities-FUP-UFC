# Questão 05
# Crie um dicionário representando os alunos de um determinado curso. O dicionário deve conter a matrícula do aluno, nome, nota da primeira prova,
# nota da segunda prova e nota da terceira prova.
# ◦ Permita ao usuário entrar com os dados de 5 alunos.
# ◦ Encontre o aluno com maior nota da primeira prova.
# ◦ Encontre o aluno com maior média geral.
# ◦ Encontre o aluno com menor média geral.
# ◦ Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 7 para aprovação.

# Solução do exercício

def main():
    alunos = []

    for _ in range(5):
        matricula = input().strip()
        nome = input().strip()
        nota1 = float(input().strip())
        nota2 = float(input().strip())
        nota3 = float(input().strip())

        aluno = {
            'matricula': matricula,
            'nome': nome,
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3
        }
        alunos.append(aluno)

    maior_nota1 = -1
    nome_maior_nota1 = ""

    maior_media = -1
    nome_maior_media = ""
    menor_media = 999
    nome_menor_media = ""

    for aluno in alunos:
        media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3

        if aluno['nota1'] > maior_nota1:
            maior_nota1 = aluno['nota1']
            nome_maior_nota1 = aluno['nome']

        if media > maior_media:
            maior_media = media
            nome_maior_media = aluno['nome']

        if media < menor_media:
            menor_media = media
            nome_menor_media = aluno['nome']

    print(f"Aluno {nome_maior_nota1} tem a maior nota1: {maior_nota1:.2f}")
    print(f"Aluno {nome_maior_media} tem a maior media: {maior_media:.2f}")
    print(f"Aluno {nome_menor_media} tem a menor media: {menor_media:.2f}")

    for aluno in alunos:
        media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3
        status = "aprovado" if media >= 7 else "reprovado"
        print(f"Aluno {aluno['nome']} esta {status} com media {media:.2f}")


if __name__ == "__main__":
    main()