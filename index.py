
cadastro = []

def cadastrar(): 
    name = input('Digite aqui seu nome: ')
    birthday = input('Digite sua data de nascimento: ')
    cpf = input('Digite seu CPF: ')
    
    for pessoa in cadastro:
        if pessoa['cpf'] == cpf:
            print('CPF já cadastrado no sistema, tente novamente.')
            return cadastrar()
    
    pessoa = {
        'nome': name,
        'nascimento': birthday,
        'cpf': cpf
    }

    cadastro.append(pessoa)
    print('Cadastro realizado com sucesso!\n')

cadastrar()
print(cadastro)


