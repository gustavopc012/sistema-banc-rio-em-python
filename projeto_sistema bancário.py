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


def obter_valor(mensagem):
    while True:
        valor_input = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(valor_input)
            if valor <= 0:
                print("Por favor, insira APENAS valores maiores que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida, informe apenas números!!")

while True:
    opcao = input(menu)

    if opcao == "d":
       
        valor = obter_valor("Informe o valor do depósito: ")

        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "s":
        
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            valor = obter_valor("Informe o valor do saque: ")

            if valor > saldo:
                print(f"Operação falhou! Saldo insuficiente (Saldo disponível: R$ {saldo:.2f}).")
            elif valor > limite:
                print(f"Operação falhou! Valor passa do limite de R$ {limite:.2f} por saque.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        # EXTRATO
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        # SAIR
        print("Obrigado por usar nosso sistema.")
        break

    else:
        print("Operação inválida.")

