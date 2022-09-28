print("\nExercício 53 - Exercício 54 rebaixado")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    valores = []

    for i in range(0, 10, 1):
        valores.append(float(input("{}º valor: ".format(i + 1))))

    const = float(input("\nConstante multiplicativa: "))

    print("\n")

    for i in range(0, 10, 1):
        valores[i] = valores[i] * const
        print("{}º Resultado: {}".format(i + 1, valores[i]))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")