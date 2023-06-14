lista1 = [1, 0, -32, 90, 500]
lista2 = [1, 2, 3, 4, 5]
lista3 = [1, 2, 3, 4, -5, 6, -7, 8, 9]

for num in lista1:
    negativos = []
    if num < 0:
        negativos.append(num)

    if len(negativos) > 0:
        print("Existe pelo menos um número negativo na lista 1")
        break

for num in lista2:
    negativos = []
    if num < 0:
        negativos.append(num)

    if len(negativos) > 0:
        print("Existe pelo menos um número negativo na lista 2")
        break

for num in lista3:
    negativos = []
    if num < 0:
        negativos.append(num)

    if len(negativos) > 0:
        print("Existe pelo menos um número negativo na lista 3")
        break