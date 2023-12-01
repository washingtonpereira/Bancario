menu = """

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair


=> """

saldo = 0
limite = 500
extrato =""
numero_saques = 0
limite_saques = 3





while True:

    opcao = input(menu)
    if opcao =="d":
        valor= float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato +=f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! Valor informado inválido.")
                
    elif opcao =="s":
       valor= float(input("Digite o valor a ser Sacado: "))
       excedeu_saldo = valor > saldo
       execedeu_limite = valor > limite
       excedeu_saques = numero_saques >= limite_saques

       if excedeu_saldo:
           print("Operação não realizada por saldo insuficiente.")

       elif execedeu_limite:
           print("Operação falhou! o Valor de saque excede o limite.")    
       elif excedeu_saques:
           print("Operação falhou! Numero de saques excedido.")    
    
       elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques +=1

       else:
           print("Operação Falhou o valor finformado é inválido.")

    elif opcao =="e":
        print("\n*********************Extrato*********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("***************************************************")
    elif opcao == "q":
        break
    else:
        print("Opção Inválida")                