print("\nExercício 52 - Exibir o maior valor do vetor")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    valores = [float(input("1º valor: "))]

    maior = valores[0]

    for i in range(1, 10, 1):
        valores.append(float(input("{}º valor: ".format(i + 1))))

        if(valores[i] > maior):
            maior = valores[i]
    
    print("\nMaior valor: {}".format(maior))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")