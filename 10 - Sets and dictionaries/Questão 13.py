# Questão 13
# Peça ao usuário para digitar seus dados pessoais (Nome, Endereço, Data de Nascimento, Cidade, CEP, email), 
# verifique se as informações de Data de Nascimento, CEP e email fazem sentido, e mostre ao usuário as informações, se estão todas corretas, 
# ou mostre que alguma informação estava errada.

# Solução do exercício

import re

def data_certa(dicionario):
    fatiamento = dicionario['nascimento'].split('/')
    if len(fatiamento[0]) == 2 and len(fatiamento[1]) == 2 and len(fatiamento[2]) == 4 and fatiamento[0].isdigit() and fatiamento[1].isdigit() and fatiamento[2].isdigit():
        return True
    else:
        print('Data errada')
        return False

def cep_certo(dicionario):
    ifem = dicionario['cep'].replace('.', '-')
    numerico = ifem.replace('-', '')
    fatiamento = ifem.split('-')
    if len(fatiamento[0]) == 2 and len(fatiamento[1]) == 3 and len(fatiamento[2]) == 3 and numerico.isdigit():
        return True
    else:
        print('CEP errado')
        return False

def email_certo(dicionario):
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(regex, dicionario['email']):
        return True
    else:
        print('E-mail errado')
        return False

def validardicionario(dicionario):
    if not data_certa(dicionario):
        return False
    if not cep_certo(dicionario):
        return False
    if not email_certo(dicionario):
        return False
    return True

dicionario = {}
dicionario['nome'] = input()
dicionario['endereco'] = input()
dicionario['nascimento'] = input()
dicionario['cidade'] = input()
dicionario['cep'] = input()
dicionario['email'] = input()

if validardicionario(dicionario):
    print(dicionario)
