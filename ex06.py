from random import randint

numeros = [randint(0, 100) for num in range(100)]

div2 = [num for num in numeros if num % 2 == 0]

while True:
    nu