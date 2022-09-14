print("\nExercício 21 - Calculadora")

r = "s"

while(r == "s"):

    print ("")
    #O exercício começa aqui
    
    v1 = float(input("Primeiro valor: "))
    v2 = float(input("Segundo valor: "))

    operacao = str(input("\n1 - Multiplicação\n2 - Adição\n3 - Divisão\n4 - Subtração\n5 - Fim do processo\n\n"))

    res = 0
    erro = 0

    if(operacao == "1"):
        res = v1 * v2
    elif(operacao == "2"):
        res = v1 + v2
    elif(operacao == "3" and (v2 != 0)):
        res = v1 / v2
    elif(operacao == "4"):
        res = v1 - v2
    elif(operacao == "5"):
        erro = 1
        break
    else:
        erro = 1
        print("[ERRO] Houve um erro durante o processo.")

    if(erro == 0):
        print("\nResultado: ", res)

    #O exercício termina aqui
    r = input("\nRepetir(s/n)? ")

print("\nProcesso finalizado.\n")