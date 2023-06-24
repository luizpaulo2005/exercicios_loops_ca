from random import randint

lista = [randint(1, 100) for i in range(100)]
lista2 = ["João", "Maria", "José", "Pedro", "Ana", "Paulo", "Lucas", "Marta", "Carlos", "Mariana"]

lista2.sort()

lista3 = [1, 2, 3]
lista4 = [4, 5, 6]

lista3.append(lista4)

print(lista3)