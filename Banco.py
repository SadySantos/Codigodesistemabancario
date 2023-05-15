menu = """

*----- Bem-vindo ao Banco Tatu. ----*

Escolha qual operação deseja realizar:

[1] Depositar

[2] Sacar

[3] Extrato

[4] Sair


=> """


saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3


while True:

    opcao = input(menu)
    
    if opcao == "1":
        dep = (float(input('Qual valor do depósito: R$')))
        
        if dep > 0:
            saldo += dep
            print('Depósito realizado com sucesso!')
            extrato+= f'Depósito: R${dep:.2f}\n'
        else:
            print('Operação falhou. Digite um valor válido!')

    elif opcao == "2":
        sq=(float(input("Qual valor você deseja sacar?")))

        excedeu_saldo = sq > saldo

        excedeu_limite = sq > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou o valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif sq > 0:
            saldo -= sq
            extrato += f'Saque: R$ 1{sq:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor é inválido.')

    elif opcao == "3":
        depositos = saldo
        print('\n--------------- EXTRATO ---------------')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('-------------------------------------')

    elif opcao == "4":
        break

    else:
        print('Operação inválida, por favor selecione a operação desejada.1')
    
                