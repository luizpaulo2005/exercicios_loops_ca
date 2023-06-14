lista = []

while len(lista) < 10:
    numbers = float(input("Digite um número: "))
    if numbers < 0:
        print("Insira um número maior que 0")
    else:
        lista.append(numbers)

soma = sum(lista)
print(f"A soma dos números da lista é {soma}")
