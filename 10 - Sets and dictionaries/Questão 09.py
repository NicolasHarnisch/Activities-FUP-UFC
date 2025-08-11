# Questão 09
# Faça um programa que armazene em um dicionário os dados de um funcionário de uma empresa, compostos de: Nome, Idade, Sexo (M/F), CPF, Data de Nascimento, 
# Código do Setor onde trabalha (0-99), Cargo que ocupa (string de até 30 caracteres) e Salário. Os dados devem ser digitados pelo usuário, 
# armazenados no dicionário e exibidos na tela.

# Solução do exercício

def coletar_dados_funcionario():
    nome = input()
    idade = int(input())
    sexo = input().upper()
    cpf = input()
    nascimento = input()
    setor = int(input())
    cargo = input()[:50]
    salario = float(input())

    funcionario = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'cpf': cpf,
        'nascimento': nascimento,
        'setor': setor,
        'cargo': cargo,
        'salario': salario
    }

    return funcionario

def main():
    funcionario = coletar_dados_funcionario()
    print(funcionario)

if __name__ == "__main__":
    main()