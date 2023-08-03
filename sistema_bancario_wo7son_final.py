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
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado:"))

        excedente_saldo = valor > saldo
        excedente_limite = valor > limite
        excedente_saques = numero_saques >= LIMITES_SAQUES

        if excedente_saldo:
            print("Operação não realizada. Você não possui saldo suficiente.")

        elif excedente_limite:
            print("Operação não realizada. O valor do saque excedeu o limite.")

        elif excedente_saques:
            print("Operação não realizada. O limite diário de saques foi atingido.")


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada. Informe um valor válido.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Nenhuma movimentação realizada até o momento." if (not extrato) else (extrato))
        # not extrato é a mesma coisa que extrato vazio.
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        print("Obrigado por escolher os nossos serviços! Até breve!")
        break

    else:
        print("Operação não realizada. Selecione uma opção válida.")







