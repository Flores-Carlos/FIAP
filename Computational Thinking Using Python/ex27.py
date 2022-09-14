print("\nExercício 27 - Se Par Soma 5, se Ímpar soma 8")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    n = int(input("Número inteiro: "))

    if(n % 2 == 0):
        print("PAR: ", n + 5)
    else:
        print("ÍMPAR: ", n + 8)

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")