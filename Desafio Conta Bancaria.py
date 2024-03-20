menu = """
[d] depositar
[s] sacar
[e] extrato]
[q] sair
"""

saldo = float(0)
limite = 500
extrato = ""
LIMITE_SAQUES = 3
tentativas_saques = 0
numero_saques = 0

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Digite o valor do deposito:")
        deposito = float(input())
        if deposito > 0:
            saldo += deposito
            print(saldo)
        else:
            print("Por favor digite um valor válido !")

    elif opcao == "s":
        print("Digite o valor do saque:")
        saque = float(input())
        tentativas_saques += 1
        numero_saques = tentativas_saques - 1

        if saque > saldo:
            print("Valor maior que o saldo em conta !")

        elif saque <= saldo and saque > 500.00:
            print("Valor de saque excedido, por favor insira um valor menor ou igual a R$ 500.00.")

        elif saque <= saldo and saque < 500.00 and tentativas_saques <= LIMITE_SAQUES:
                saldo =  saldo - saque
                print("Saque realizado com sucesso")
                print(f"Saldo:{saldo}")
        else:
            print("Número de saques excedido no dia !")



    elif opcao == "e":
        extrato = (f"Saldo:{saldo}\n Limite por saque:{limite}\n Limite de saques: {LIMITE_SAQUES}\n Número de saques: {numero_saques}")
        print("---------------- EXTRATO ----------------")
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, digite uma opção correta !")
