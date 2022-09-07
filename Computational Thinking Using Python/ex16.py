print ("")
print("Exercício 16 - Forma um triângulo retângulo?")

r = "s"

while(r == "s"):

    print ("")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    c = float(input("3º valor: "))

    hip = 0
    cat1 = 0
    cat2 = 0

    if(a > b):
        if(a > c):
            hip == a
            cat1 == b
            cat2 == c
        elif(b > c):
            hip == b
            cat1 == a
            cat2 == c
        else:
            hip == c
            cat1 == a
            cat2 == b
    elif(b > c):
        hip == b
        cat1 = a
        cat2 == c
    else:
        hip == c
        cat1 == a
        cat2 == b
    
    if((hip ** 2) == (cat1 ** 2) + (cat2 ** 2)):
        print("Forma um triângulo retângulo")
    else:
        print("NÃO forma um triângulo retângulo")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")