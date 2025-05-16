Menu =  """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo  = 0
Limite = 500
extrato  =""
numero_de_saques = 0
limite_de_saques = 3
while True:
    opçao = input(Menu).strip().lower()
    
    if opçao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Você não pode inserir valor menores que zero ou negativos")
            
    elif opçao == "s":
        valor = float(input("Informe o quanto deseja sacar: "))
        
        if numero_de_saques > limite_de_saques:
            print(f"Você não pode sacar mais de 3 vezes ao dia")
        if saldo <valor:
            print(f"Você não tem dinheiro o suficiente para realizar este saque.")   
        else: 
            if valor>500:
                print(f"Você não pode sacar mais que R$500.\nO valor inserido foi de R${valor}") 
            elif valor >0 and valor<=500:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_de_saques +=1
            else:
                print(f"Você não pode sacar valores negativos ou Iguais a 0")          
                
    elif opçao == "e":
        print("\n==========Extrato==========")
        print(f"Não foram realizadas movimentações ainda"if not extrato else extrato)
        print(f"Saldo = R${saldo}")        
        print("===========================")
        
    elif opçao == "q":
        print(f"Você escolheu sair.")
        break
    
    else:
        print(f"Insira algo válido do menu.")