# Crie uma lista com 100 números aleatórios. Percorra esta lista e imprima a posição e o valor do primeiro elemento contido na lista que seja par, e a posição e o valor do elemento imediatamente após este elemento.

from random import randint

lista = [randint(1, 100) for i in range(100)]

valor_atual = 0
valor_anterior = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        valor_atual = i
        valor_anterior = i - 1
        print(f'Elemento Atual: {valor_atual} - Valor: {lista[valor_atual]}')
        print(f'Elemento Anterior: {valor_anterior} - Valor: {lista[valor_anterior]}')
        break