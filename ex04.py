from random import randint

numeros = [randint(1, 100) for num in range(10)]
print(numeros)

maior_num = numeros[0]
menor_num = numeros[0]

for num in numeros:
    if num < menor_num:
        menor_num = num

    if num > maior_num:
        maior_num = num

print(f"{maior_num}")
print(f"{menor_num}")