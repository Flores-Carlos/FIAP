print ("")
print("Exercício 10 - Exibir o maior valor ou se são idênticos")

r = "s"

while(r == "s"):

    print ("")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))

    if(a > b):
        print("Maior valor: ", a)
    elif(b > a):
        print("Maior valor: ", b)
    else:
        print("Valores idênticos")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")