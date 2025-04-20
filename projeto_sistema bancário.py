menu = """

[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_input = input("Informe o valor do depósito: ")

        
        valor_input = valor_input.replace(",", ".")

        try:
            valor = float(valor_input)

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"  
            else:
                print("Operação falhou, o valor informado é inválido.")
        except ValueError:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            valor = float(input("Informe o valor do saque: "))

            if valor <= 0:
                print("Operação falhou! Valor inválido.")
            elif valor > saldo:
                print("Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                print("Operação falhou! Valor excede o limite de R$ 500,00.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
