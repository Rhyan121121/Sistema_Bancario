import textwrap
def menu():
    menu =  """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo usúario
    [q] Sair

    """
    return input(menu)
def main():
    
    saldo  = 0
    limite = 500
    extrato  =""
    numero_de_saques = 0
    limite_de_saques = 3
    contas = []
    usuarios = []
    agencia = "0001"
    while True:
        opçao = menu()
        
        if opçao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo , extrato = deposito(saldo, valor, extrato)
                
        elif opçao == "s":
            valor = float(input("Informe o quanto deseja sacar: "))
            
            saldo , extrato, numero_de_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_de_saques, 
                limite_saques=limite_de_saques
            )     
                    
        elif opçao == "e":
           Extrato(saldo, extrato=extrato)
            
        elif opçao == "q":
            print(f"Você escolheu sair.")
            break
        
        elif opçao == "lc":
            listar_contas(contas)
        elif opçao == "nu":
            criar_usuario(usuarios)
        elif opçao == "nc":
            numero_conta = len(contas) + 1  
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            else:
                print(f"Insira algo válido do menu.")
            
        
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"Depósito Realizado")
    else:
        print("Você não pode inserir valores menores ou iguais a zero")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print(f"Você não pode sacar mais de {limite_saques} vezes ao dia")
    elif valor > saldo:
        print(f"Você não tem dinheiro o suficiente para realizar este saque.")
    elif valor > limite:
        print(f"Você não pode sacar mais que R${limite}.\nO valor inserido foi de R${valor}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print(f"Você não pode sacar valores negativos ou iguais a 0")
    return saldo, extrato, numero_saques

def Extrato(saldo, /, *, extrato):
    print("==========Extrato==========")
    print(f"Não foram realizadas movimentações ainda"if not extrato else extrato)
    print(f"Saldo = R${saldo}")
    print("===========================")
        
        
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = filtrar_usuario(cpf, usuarios)

    if usuario_existente:
        print("Já existe usuário com esse CPF!")
        return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print(f"Usuário criado com sucesso!")
    
def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    
def filtrar_usuario(cpf, usuario):
    usuario_filtrado = [usuario for usuario in usuario if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

main()