print ("")
print("Exercício 12 - Área de um retângulo + Avisos")

r = "s"

while(r == "s"):

    print ("")
    altura = float(input("Altura(m) do retângulo: "))
    base = float(input("Base(m) desse retângulo: "))
    area = base * altura

    print("Área: ", area, "m²")

    if(area > 100):
        print("Aviso: terreno grande")
    else:
        print("Aviso: terreno pequeno")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")