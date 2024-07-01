# Sistema Bancário com Interface Gráfica

Este é um projeto de um sistema bancário simples com uma interface gráfica desenvolvida em Python usando a biblioteca `tkinter`. O sistema permite realizar operações bancárias básicas como depósitos, saques, visualização de extrato, criação de usuários e contas correntes.

## Funcionalidades

- **Depósito:** Permite depositar um valor na conta.
- **Saque:** Permite sacar um valor da conta, respeitando limites de saldo, valor e número de saques diários.
- **Extrato:** Exibe o extrato das movimentações e o saldo atual.
- **Criar Usuário:** Permite criar novos usuários com nome, data de nascimento, CPF e endereço.
- **Criar Conta Corrente:** Permite criar contas correntes vinculadas a usuários existentes.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído por padrão com a instalação do Python)

## Instalação

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd sistema-bancario
    ```

3. (Opcional) Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Execute o script principal:
    ```bash
    python main.py
    ```

## Uso

1. Abra o aplicativo e insira o valor desejado para depósito ou saque.
2. Clique nos botões para realizar depósitos, saques, visualizar extrato, criar usuários ou criar contas correntes.
3. Para criar um usuário, preencha os campos na janela de criação de usuário e clique em "Salvar".
4. Para criar uma conta corrente, insira o CPF do usuário existente e clique em "Salvar".

## Estrutura do Projeto

```plaintext
sistema-bancario/
│
├── main.py          # Script principal com a interface gráfica
├── README.md        # Este arquivo README
└── ...
