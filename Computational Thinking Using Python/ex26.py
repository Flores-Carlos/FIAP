print("\nExercício 25 - Par ou Ímpar?")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    n = float(input("Número: "))

    if(n >= 0):
        print("Dobro: ", n * 2)
    else:
        print("Triplo: ", n * 3)
        
    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")