print("\nExercício 54 - Multiplicação de uma constante por um vetor")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    num = []
    res = []

    for i in range(0, 20, 1):
        x = float(input("{}º valor: ".format(i + 1)))
        num.append(x)

    mult = float(input("\nDigite o multiplicador: "))

    print("\n")

    for i in range(0, 20, 1):
        res.append(num[i] * mult)
        print("{}º resultado: {}".format(i + 1, res[i]))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")