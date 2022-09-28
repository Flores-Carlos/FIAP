print("\nExercício 56 - Armazenar e exibir nome e idade")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    nome = []
    idade = []

    for i in range(0, 100, 1):
        nome.append(input("\nNome da {}º pessoa: ".format(i + 1)))
        idade.append(int(input("Idade da {}º pessoa: ".format(i + 1))))
        while(idade[i] < 0):
            idade[i] = int(input("[ERRO] Digite novamente: "))

    print()

    for i in range(0, 100, 1):
        print("{}ª pessoa: {}, {} anos".format(i + 1, nome[i], idade[i]))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")