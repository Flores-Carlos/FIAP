print ("")
print("Exercício 11 - Área de um retângulo + Aviso")

r = "s"

while(r == "s"):

    print ("")
    altura = float(input("Altura(m) do retângulo: "))
    base = float(input("Base(m) desse retângulo: "))
    area = base * altura

    print("Área: ", area, "m²")

    if(area > 100):
        print("Aviso: terreno grande")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")