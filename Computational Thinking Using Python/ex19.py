print ("")
print("Exercício 19 - Duas avaliações com pesos diferentes")

r = "s"

while(r == "s"):

    print ("")
    p1 = float(input("Nota da P1: "))
    while(p1 < 0 or p1 > 10):
        p1 = float(input("Inválido. Digite novamente: "))
    p2 = float(input("Nota da P2: "))
    while(p2 < 0 or p2 > 10):
        p2 = float(input("Inválido. Digite novamente: "))

    media = (p1 + 2 * p2) / 3

    print(media >= 5 and "Aprovado" or "Reprovado")

    print ("")
    r = input("Repetir(s/n)? ")

print ("")
print("Processo finalizado.")
print ("")