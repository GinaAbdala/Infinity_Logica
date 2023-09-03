aculador_notas = 0
voltas = 0

aculador_notas = 0
voltas = 0

while True:
    nota = input("Digite a nota: ")

    if nota not in "012345678910:":
        print ("nota invalida")
    else:
        nota = float(nota)

        if nota >= 0 and nota <= 10:
            aculador_notas += nota
            voltas += 1

            escolha = input("Quer adionar mais uma nota?(s/n) ")

            if escolha.lower() == 'n' or escolha.lower() == "não":
                break
        else:
            print("Notas apenas entre 0 e 10")

media = aculador_notas / voltas

print(media)