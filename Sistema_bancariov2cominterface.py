import tkinter as tk
from tkinter import messagebox

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

# Funções do sistema bancário
def sacar(saldo, valor, extrato, limite, limite_saques, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        messagebox.showerror("Erro", "Você não tem saldo suficiente.")
    elif excedeu_limite:
        messagebox.showerror("Erro", "O valor do saque excede o limite.")
    elif excedeu_saques:
        messagebox.showerror("Erro", "Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")
    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    extrato_msg = "Não foram realizadas movimentações." if not extrato else extrato
    messagebox.showinfo("Extrato", f"{extrato_msg}\n\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    def salvar_usuario():
        cpf = cpf_entry.get()
        usuario_existente = next((user for user in usuarios if user['cpf'] == cpf), None)

        if usuario_existente:
            messagebox.showerror("Erro", "Usuário já existente!")
            return

        nome = nome_entry.get()
        data_nascimento = nascimento_entry.get()
        endereco = endereco_entry.get()

        usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        })

        messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
        user_window.destroy()

    user_window = tk.Toplevel()
    user_window.title("Criar Usuário")

    tk.Label(user_window, text="CPF:").grid(row=0, column=0)
    cpf_entry = tk.Entry(user_window)
    cpf_entry.grid(row=0, column=1)

    tk.Label(user_window, text="Nome:").grid(row=1, column=0)
    nome_entry = tk.Entry(user_window)
    nome_entry.grid(row=1, column=1)

    tk.Label(user_window, text="Data de Nascimento:").grid(row=2, column=0)
    nascimento_entry = tk.Entry(user_window)
    nascimento_entry.grid(row=2, column=1)

    tk.Label(user_window, text="Endereço:").grid(row=3, column=0)
    endereco_entry = tk.Entry(user_window)
    endereco_entry.grid(row=3, column=1)

    tk.Button(user_window, text="Salvar", command=salvar_usuario).grid(row=4, column=0, columnspan=2)

def criar_conta_corrente(agencia, contas, usuarios):
    def salvar_conta():
        cpf = cpf_entry.get()
        usuario = next((user for user in usuarios if user['cpf'] == cpf), None)

        if not usuario:
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return

        numero_conta = len(contas) + 1
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })

        messagebox.showinfo("Sucesso", f"Conta corrente {numero_conta} criada com sucesso!")
        account_window.destroy()

    account_window = tk.Toplevel()
    account_window.title("Criar Conta Corrente")

    tk.Label(account_window, text="CPF do Usuário:").grid(row=0, column=0)
    cpf_entry = tk.Entry(account_window)
    cpf_entry.grid(row=0, column=1)

    tk.Button(account_window, text="Salvar", command=salvar_conta).grid(row=1, column=0, columnspan=2)

# Interface gráfica principal
def main():
    def depositar_callback():
        global saldo, extrato
        valor = float(valor_entry.get())
        saldo, extrato = depositar(saldo, valor, extrato)
        messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")

    def sacar_callback():
        global saldo, extrato, numero_saques
        valor = float(valor_entry.get())
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)
        messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")

    def extrato_callback():
        global saldo, extrato
        mostrar_extrato(saldo, extrato)

    def criar_usuario_callback():
        criar_usuario(usuarios)

    def criar_conta_corrente_callback():
        criar_conta_corrente("0001", contas, usuarios)

    root = tk.Tk()
    root.title("Sistema Bancário")

    tk.Label(root, text="Valor:").grid(row=0, column=0)
    valor_entry = tk.Entry(root)
    valor_entry.grid(row=0, column=1)

    tk.Button(root, text="Depositar", command=depositar_callback).grid(row=1, column=0, columnspan=2)
    tk.Button(root, text="Sacar", command=sacar_callback).grid(row=2, column=0, columnspan=2)
    tk.Button(root, text="Extrato", command=extrato_callback).grid(row=3, column=0, columnspan=2)
    tk.Button(root, text="Criar Usuário", command=criar_usuario_callback).grid(row=4, column=0, columnspan=2)
    tk.Button(root, text="Criar Conta Corrente", command=criar_conta_corrente_callback).grid(row=5, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
