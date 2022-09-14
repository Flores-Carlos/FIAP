print("\nExercício 23 - (A + B < C)?")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    a = int(input("Valor A: "))
    b = int(input("Valor B: "))
    c = int(input("Valor C: "))

    print("(A + B < C)?")

    if((a + b) < c):
        print("SIM")
    else:
        print("NÃO")
    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")