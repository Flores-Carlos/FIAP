print("\nExercício 55 - Procurar dentro do vetor")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    val = []
    encontrou = 0

    vet = int(input("Número de valores permitidos dentro do vetor (máx. 20): "))

    while(vet > 20):
        vet = int(input("\n[ERRO] Digite novamente: "))

    print()

    for i in range(0, vet, 1):
        val.append(float(input("{}º valor: ".format(i + 1))))

    consulta = float(input("\nValor a ser procurado dentro do vetor: "))

    for i in range(0, vet, 1):
        if(val[i] == consulta):
            encontrou = 1
            print("\n{}º valor, posição {} do vetor.".format(i + 1, i))

    if(not encontrou):
        print("\nValor não encontrado dentro do vetor.")

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")