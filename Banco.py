contas = {}

def criar_conta():
    numero = input("Número da conta: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    tipo = input("Tipo (Poupança/Conta Corrente): ")
    saldo = float(input("Saldo inicial: "))
    contas[numero] = [nome, idade, tipo, saldo]
    print("Conta criada com sucesso.")

def depositar():
    numero = input("Número da conta: ")
    valor = float(input("Valor do depósito: "))
    if numero in contas:
        contas[numero][3] += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def sacar():
    numero = input("Número da conta: ")
    valor = float(input("Valor do saque: "))
    if numero in contas and contas[numero][3] >= valor:
        contas[numero][3] -= valor
        print("Saque realizado com sucesso.")
        if contas[numero][3] < 500:
            print("Atenção: saldo baixo.")
    else:
        print("Saldo insuficiente ou conta não encontrada.")

def verificar_saldo():
    numero = input("Número da conta: ")
    if numero in contas:
        print("Saldo atual:", contas[numero][3])
    else:
        print("Conta não encontrada.")

def visualizar_todas_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("\nDetalhes de todas as contas:")
        for numero, dados in contas.items():
            print(f"Conta: {numero}")
            print(f"  Nome: {dados[0]}")
            print(f"  Idade: {dados[1]}")
            print(f"  Tipo: {dados[2]}")
            print(f"  Saldo: {dados[3]}")
            print("-" * 30)


while True:
    print("\n1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver Saldo")
    print("5. Sair")
    print("6. Ver Todas as Contas")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        criar_conta()
    elif escolha == '2':
        depositar()
    elif escolha == '3':
        sacar()
    elif escolha == '4':
        verificar_saldo()
    elif escolha == '5':
        break
    elif escolha == '6':
        visualizar_todas_contas()
    else:
        print("Opção inválida.")
