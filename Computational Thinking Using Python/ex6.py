print ("")
print("Exercício 6 - Conversão de Dólar para Real")

r = "s"

while(r == "s"):

    print ("")
    cotacaoDolar = float(input("Digite a atual cotação do Dólar: "))
    valorDolares = float(input("Digite o valor($) que deseja converter para Real: "))

    valorReais = cotacaoDolar * valorDolares

    print("R$", valorReais)

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")