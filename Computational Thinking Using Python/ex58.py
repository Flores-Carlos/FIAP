print("\nExercício 58 - Exercício 57, porém exibindo o número de pessoas com mais de 18 anos")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    nome = []
    idade = []
    sexo = []
    qtd = 0

    for i in range(0, 3, 1):
        nome.append(input("\nNome da {}º pessoa: ".format(i + 1)))
        sexo.append(input("Sexo (m/f) da {}ª pessoa: ".format(i + 1)))
        while(sexo[i] != "m" and sexo[i] != "f"):
            sexo[i] = input("[ERRO] Digite novamente: ")
        idade.append(int(input("Idade da {}º pessoa: ".format(i + 1))))
        while(idade[i] < 0):
            idade[i] = int(input("[ERRO] Digite novamente: "))

    print()

    for i in range(0, 3, 1):
        if(idade[i] > 18):
            print("{}ª pessoa: {}, {}, {} anos".format(i + 1, nome[i], (sexo[i] == "m" and "Homem" or "Mulher"), idade[i]))

            qtd += 1

    print("\n{} pessoa(s) possuem a idade superior a 18 anos.".format(qtd))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")