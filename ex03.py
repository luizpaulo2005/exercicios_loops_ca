number_input = 1
numbers_list = []

while number_input >= 0:
    number_input = int(input("Insira um número, digite um valor abaixo de 0 para parar a execução da aplicação: "))
    numbers_list.append(number_input)

numbers_list.pop()
print(numbers_list)