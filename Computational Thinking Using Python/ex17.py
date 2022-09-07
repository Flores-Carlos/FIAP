print ("")
print("Exercício 17 - Peso ideal de novo")

r = "s"

while(r == "s"):

    print ("")
    sexo = input("Sexo(m/f): ")
    while(sexo != "m" and sexo != "f"):
        sexo = input("Valor inválido. Digite novamente: ")
    peso = float(input("Peso(Kg): "))
    altura = float(input("Altura(m): "))

    imc = peso / (altura ** 2)

    if(sexo == "m"):
        if(imc < 20):
            print("Abaixo do peso")
        elif(imc >= 20 and imc < 25):
            print("Peso ideal")
        elif(imc >= 25):
            print("Acima do peso")
    else:
        if(imc < 19):
            print("Abaixo do peso")
        elif(imc >= 19 and imc < 24):
            print("Peso ideal")
        elif(imc >= 24):
            print("Acima do peso")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")