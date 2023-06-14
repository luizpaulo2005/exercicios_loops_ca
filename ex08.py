numeros = [num for num in range(10)]
numeros_reverso = []
i = 0
n = len(numeros) - 1


while i < len(numeros):
    numeros_reverso.append(numeros[n])
    i += 1
    n -= 1

print(numeros_reverso)