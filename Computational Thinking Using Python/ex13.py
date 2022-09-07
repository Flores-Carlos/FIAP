print ("")
print("Exercício 13 - Exibir o maior valor (de 3 valores)")

r = "s"

while(r == "s"):

    print ("")
    a = int(input("1º valor: "))
    b = int(input("2º valor: "))
    c = int(input("3º valor: "))
    
    if(a > b):
        if(a > c):
            print("Maior valor: ", a)
        elif(b > c):
            print("Maior valor: ", b)
        else:
            print("Maior valor: ", c)
    elif(b > c):
        print("Maior valor: ", b)
    else:
        print("maior valor: ", c)
        
    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")