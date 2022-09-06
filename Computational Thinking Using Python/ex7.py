print ("")
print("Exercício 7 - Troco de cinco produtos")

r = "s"

while(r == "s"):

    print ("")
    precoTotal = 0
    for i in range(1, 6, 1):
        produto = float(input("Valor do {}º produto: ".format(i)))

        precoTotal += produto

    print("Total: ", precoTotal)

    dinheiro = float(input("Valor(R$) em dinheiro entregue pelo cliente: "))

    if(dinheiro < precoTotal):
        print("Valor insuficiente.")
    else:
        print("Troco: R$", (dinheiro - precoTotal))
        
    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")