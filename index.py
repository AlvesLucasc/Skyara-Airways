import random

cadastro = []

def cadastrar(name, birthday, cpf): 
    name = input('Digite aqui seu nome: ')
    birthday = int(input('Digite sua data de nascimento: '))
    cpf = float(input('Digite seu cpf contendo "." e "-"'))
    name.append(cadastro)
    birthday.append(cadastro)
    if cpf in cadastro:
        print('Cpf já cadastrado no sistema, tente novamente')
        return cadastrar():


