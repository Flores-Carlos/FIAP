print("\nExercício 30 - ...")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    nomeProduto = str(input("Produto: "))
    precoProduto = float(input("Preço(R$): "))

    formaPag = str(input("\nCódigo de condição de pagamento: \n\n1 - À vista em dinheiro ou cheque, recebe 10% de desconto \n2 - À vista no cartão de crédito, reebe 15% de desconto \n3 - Em duas vezes, preço normal de etiqueta sem juros \n4 - Em quatro vezes, preço normal de etiqueta mais juros de 10%\n"))
    while(formaPag > 4 or formaPag < 1):
        formaPag = str(input("Opção inválida. Digite novamente: "))

    if(formaPag == "1"):
        precoProduto -= precoProduto * 0.1
    elif(formaPag == "2"):
        precoProduto -= precoProduto * 0.15
    elif(formaPag == "3"):
        precoProduto = precoProduto
    elif(formaPag == "4"):
        precoProduto += precoProduto * 0.1
    else:
        print("[ERRO] Algo deu errado durante o processo.")

    print(nomeProduto, "\nValor final: R$", precoProduto)

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")