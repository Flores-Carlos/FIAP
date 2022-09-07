print ("")
print("Exercício 15 - Tipos de triãngulos")

r = "s"

while(r == "s"):

    print ("")
    
    l1 = float(input("1° lado do triângulo: "))
    l2 = float(input("2° lado do triângulo: "))
    l3 = float(input("3° lado do triângulo: "))

    if not((l1 < l2 + l3 and l1 > abs(l2 - l3))
    or (l2 < l1 + l3 and l2 > abs(l1 - l3))
    or (l3 < l1 + l2 and l3 > abs(l1 - l2))):
        print("NÃO pode ser um triângulo.")
    else:
        if(l1 == l2 and l1 == l3):
            print("Triângulo EQUILÁTERO")
        elif(l1 != l2 and l1 != l3 and l2 != l3):
            print("Triângulo ESCALENO")
        elif(l1 == l2 and l1 != l3
        or   l2 == l3 and l2 != l1
        or   l3 == l1 and l3 != l2):
            print("Triângulo ISÓSCELES")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")