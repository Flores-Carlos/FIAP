print("\nExercício 22 - Cálculo de área")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    sel = str(input("\n1 - Triângulo\n2 - Quadrado\n3 - Retângulo\n4 - Círculo\n5 - Fim do processo\n\n"))

    if(sel == '1'):
        base = float(input("Base do triângulo: "))
        altura = float(input("Altura do triângulo: "))

        res = (base * altura) / 2

        print("Área: ", res)

    elif(sel == '2'):
        lado = float(input("Lado do quadrado: "))

        res = lado * 4

        print("Área: ", res)

    elif(sel == '3'):
        base = float(input("Base do retângulo: "))
        altura = float(input("Altura do retângulo: "))

        res = base * altura

        print("Área: ", res)

    elif(sel == '4'):
        raio = float(input("Raio do círculo: "))

        res = 3.14 * (raio ** 2)

        print("Área: ", res)

    elif(sel == '5'):
        break

    else:
        print("[ERRO] Houve um problema durante o processo.")

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")