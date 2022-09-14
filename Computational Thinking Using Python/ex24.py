print("\nExercício 23 - (A + B < C)?")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    nome = str(input("Nome: "))
    sexo = str(input("Sexo (m/f): "))
    estCiv = str(input("Estado Civil: "))

    if(sexo == "f" and (estCiv == "casada" or estCiv == "CASADA")):
        tempo = str(input("Tempo de casada (anos): "))

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")