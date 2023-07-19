def pprint(mensagem: str):
  print("=" * 30)
  print(mensagem)
  print("=" * 30)


menu = """
   $=======================$
   | BEM-VINDO AO BANCO BV |
   $=======================$

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = {"deposito": [], "saque": []}
numero_saques = 1
LIMITE_SAQUES = 3

while True:
  
  opcao = input(menu).lower()

  if opcao == "d":
    deposito = int(input("Digite em números o valor do depósito: "))

    if deposito < 0:
      pprint("Valor digitado inválido, por favor tente novamente!")
    
    else:
      saldo += deposito
      extrato["deposito"].append(deposito)
      pprint("Depósito feito com sucesso!")

  elif opcao == "s":
    saque = int(input("Digite em números o valor do saque: "))

    if saque < 0 or saque > 500:
      pprint("Valor digitado inválido, por favor tente novamente!")
    
    elif saldo == 0:
      print("A operação saque não será possivel por falta de saldo!")

    else:
      if numero_saques <= LIMITE_SAQUES:
        saldo -= saque
        extrato["saque"].append(saque)
        pprint("Saque feito com sucesso!")
        numero_saques += 1
      else:
        pprint("Limite de saques atingido!")
        pass

  elif opcao == "e":
    pprint(f"EXTRATO DE HOJE".center(30, " "))

    for saques in extrato["saque"]:
      print(f"Saques: R$ {saques:.2f}")

    for depositos in extrato["deposito"]:
      print(f"Depositos: R$ {depositos:.2f}")

    pprint(f"Saldo atual: R$ {saldo:.2f}")
    

  elif opcao == "q":
    pprint("Volte sempre!")
    break

  else:
    pprint("Operação inválida, por favor selecione novamente a operação desejada.")
    