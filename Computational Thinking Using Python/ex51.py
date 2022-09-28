print("\nExercício 51 - Armazenar valores e exibir em ordem inversa")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    valores = []

    for i in range(0, 10, 1):
        valores.append(float(input("{}º valor: ".format(i + 1))))
    
    print("\n")

    for i in range(9, -1, -1):
        print("{}º valor: {}".format(i + 1, valores[i]))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")