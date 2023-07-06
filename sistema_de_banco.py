import textwrap

def menu():
    menu = '''\n
    =================== MENU ====================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    
    ==> '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print("\n ------------DEPOSITO REALIZADO COM SUCESSO---------")
    else:
        print("\n_________Operação falhou! O valor informado é inváldo.______")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >> limite_saques

    if excedeu_saldo:
        print("\n__Operação Falhou__\n___Saldo insuficiente___\n")
    
    elif excedeu_limite:
        print("\n__Operação Falhou__\n___O valor do saque execeu o limite.")
    
    elif excedeu_saques:
        print("\n_Operação Falhou__\n___Numero maximo de saques excedido.__")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print("\nOperação falhou, o valor informado é invalido...\n")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n======= EXTRATO ======\n')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR${saldo:.2f}')
    print("==================================")

    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuario com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario.append({'Nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("USUARIO CRIADO COM SUCESSO")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n===CONTA CRIADA COM CUCESSO===\n")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}


def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print("="+100)
    print(textwrap.dedent(linha))


def main():
    limite = 500
    extrato = ''
    numero_de_saques = 0
    saldo = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor= float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                limite_de_saques=LIMITE_SAQUES,
                )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break
        
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada...")


main()
