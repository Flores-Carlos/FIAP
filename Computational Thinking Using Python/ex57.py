print("\nExercício 57 - Exercício 56, mas agora só exibindo as mulheres")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    nome = []
    idade = []
    sexo = []

    for i in range(0, 100, 1):
        nome.append(input("\nNome da {}º pessoa: ".format(i + 1)))
        sexo.append(input("Sexo (m/f) da {}ª pessoa: ".format(i + 1)))
        while(sexo[i] != "m" and sexo[i] != "f"):
            sexo[i] = input("[ERRO] Digite novamente: ")
        idade.append(int(input("Idade da {}º pessoa: ".format(i + 1))))
        while(idade[i] < 0):
            idade[i] = int(input("[ERRO] Digite novamente: "))

    print()

    for i in range(0, 100, 1):
        if(sexo[i] == "f"):
            print("{}ª pessoa: {}, {}, {} anos".format(i + 1, nome[i], (sexo[i] == "m" and "Homem" or "Mulher"), idade[i]))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")