print("\nExercício 29 - Ordem Decrescente")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    v1 = int(input("1º valor inteiro: "))
    v2 = int(input("2º valor inteiro: "))
    while(v2 == v1):
        v2 = int(input("Não pode ser igual ao(s) anterior(es). Insira novamente: "))
    v3 = int(input("3º valor inteiro (diferente dos anteriores): "))
    while(v3 == v1 or v3 == v2):
        v3 = int(input("Não pode ser igual ao(s) anterior(es). Insira novamente: "))

    print("\nOrdem decrescente: \n")

    if(v1 > v2):
        if(v1 > v3):
            if(v2 > v3):
                print(v1, " > ", v2, " > ", v3)
            else:
                print(v1, " > ", v3, " > ", v2)
        else:
            print(v3, " > ", v1, " > ", v2)
    elif(v2 > v3):
        if(v1 > v3):
            print(v2, " > ", v1, " > ", v3)
        else:
            print(v2, " > ", v3, " > ", v1)
    else:
        print(v3, " > ", v2, " > ", v1)

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")