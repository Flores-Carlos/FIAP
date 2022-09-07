print ("")
print("Exercício 18 - Velocidade de um automóvel")

r = "s"

while(r == "s"):

    print ("")
    
    a = float(input("Aceleração(m/s²): "))
    v0 = float(input("Velocidade inicial(m/s): "))
    t = float(input("Tempo em segundos: "))

    v = v0 + (a * t)

    if(v <= 40):
        print("Veículo muito lento")
    elif(v > 40 and v <= 60):
        print("Velocidade permitida")
    elif(v > 60 and v <= 80):
        print("Velocidade de cruzeiro")
    elif(v > 80 and v <= 120):
        print("Veículo rápido")
    elif(v > 120):
        print("Veículo muito rápido")
    

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")