# Definição das funções

def sacar(*, saldo, valor, extrato, limite, limite_saques, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def mostrar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funções para criar usuário e conta corrente

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = next((user for user in usuarios if user['cpf'] == cpf), None)

    if usuario_existente:
        print("Usuário já existente!")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla - estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((user for user in usuarios if user['cpf'] == cpf), None)

    if not usuario:
        print("Usuário não encontrado!")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    print(f"Conta corrente {numero_conta} criada com sucesso!")

# Variáveis globais

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

# Menu principal

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        agencia = "0001"
        criar_conta_corrente(agencia, contas, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
