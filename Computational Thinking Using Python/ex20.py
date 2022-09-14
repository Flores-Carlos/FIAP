print ("")
print("Exercício 19 - Duas avaliações com pesos diferentes")

r = "s"

while(r == "s"):

    print ("")
    
    p1 = float(input("Primeira nota (P1): "))
    while(p1 < 0 or p1 > 10):
        p1 = float(input("Inválido. Digite novamente: "))

    min = 7.5 - p1 / 2

    print("Nota mínima necessária na P2: ", min)

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")