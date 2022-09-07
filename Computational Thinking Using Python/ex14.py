print ("")
print("Exercício 14 - Cálculo de peso ideal")

r = "s"

while(r == "s"):

    print ("")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    imc = peso / (altura ** 2)

    if(imc >= 18.5 and imc <= 24.9):
        print("Peso ideal")
    else:
        print("Peso NÃO ideal")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")