#\n quebra de linha

'''
    So pode depositos positivos
    Valor de saque limite : 500
    Limite de saques: 3
    Mostrar o saldo em conta
    Mostrar movimentações no extrato

'''


menu = """

   =============== MENU ==================   
    [1] Depositar
    
    [2] Sacar

    [3] Extrato
      
    [0] Sair
      
    =====================================
    Selecione ação desejada: """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto deseja depositar: "))      
 
        if deposito > 0: #verificando se o valor e maior que zero
            saldo += deposito #adicionando o deposito no saldo
            extrato += f"\nDeposito: R${deposito: .2f}" #colocando o valor depositado no extrato

        else:
            print("Operação falhou! Valor Invalido")        

    elif opcao == "2":
        valor= float(input("Valor do saque: "))
        
        saldo_insuficiente = valor > saldo #pra ver se tem saldo para sacar

        saque_excedido = valor > limite #excedeu o limite de saque

        saque_diario = numeros_saques >= limite_saque #limite de saque diario

        if saldo_insuficiente:
            print("!!! ERRO !!! Saldo insuficiente, confira o saldo da conta")
        
        elif saque_excedido:
            print("!!! ERRO !!! O valor do saque ultrapassa o limite. Tente novamente")
        
        elif saque_diario:
            print("!!! ERRO !!! Limite de saques diarios excedidos, volte amamhã")


        elif deposito > 0:
            saldo -= valor #tirando o valor sacado do saldo
            extrato += f"\nSaque: R${valor: .2f}\n" #colocando o valor sacado no extrato
            numeros_saques += 1 #adcionando mais um no numero de saque, para ele começar a contar
        else:
            ("!!! ERRO !!! Valor de saque invalido")


    elif opcao == "3":

        print("Não existem movimentações." if not extrato else extrato) #Verificando se existe movimentaçao no extrato
        print(f"\nSaldo: R$ {saldo: .2f}") # mostrando o saldo em conta


    
    
    elif opcao == "0":
        print(       " Obrigado por usar nossos serviços !         ")
        break
    
    else:
        print("--------------------[ E R R O ]------------------")
        
    
        