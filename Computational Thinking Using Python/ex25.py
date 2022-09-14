print("\nExercício 25 - Par ou Ímpar?")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    n = int(input("Número: "))

    if(n % 2 == 0):
        print("PAR")
    else:
        print("ÍMPAR")

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")