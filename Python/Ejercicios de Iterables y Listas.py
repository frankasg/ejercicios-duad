#Ejercicio 1
print("Ejericio 1: ---------------------------------------------")

first_list = ["Hay", "en", "que", "iteración", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

len_first_list = len(first_list)
len_second_list = len(second_list)

if(len_first_list != len_second_list):
    print("Error listas inválidas, ambas listas deben ser del mismo tamaño")

else:
    for index in range(len_first_list):
        print(f"{first_list[index]} {second_list[index]}")

#Ejercicio 2
print("Ejericio 2: ---------------------------------------------")

my_string  = "Pizza con piña"

for index in range(len(my_string) - 1, -1, -1):
    print(my_string[index])

#Ejercicio 3
print("Ejericio 3: ---------------------------------------------")

my_list = [4, 3, 6, 1, 7]

if(len(my_list) >= 2):
    first_number = my_list.pop(0)
    last_number = my_list.pop()

    my_list.insert(0, last_number)
    my_list.append(first_number)

print(my_list)

print("Ejericio 4: ---------------------------------------------")
#En las indicaciones del método no dice que no podamos usar remove, por lo que lo usé para hacer una implementación mas limpia
#pero en caso hacerlo con pop te lo pongo por acá en comentarios: Habria que iterar en la lista y cuando se encuentre un numero que hay que borrar
#guardar dicho numero en una variable para después buscarlo en otro for anidado y me diga cual es el indice para hacerle pop

my_even_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11,11,11,11]
iterable_list = my_even_list.copy()

for item in iterable_list:
    if(item % 2 != 0):
        my_even_list.remove(item) 

print(my_even_list)

print("Ejericio 5: ---------------------------------------------")

user_input = input("Ingrese 10 números separada unicamente por comas y sin espacios ejemplo (50,90,100,75...):")
numbers = [int(num) for num in user_input.split(',')]
max_number = 0

for item in numbers:
    if(item > max_number):
        max_number = item

print(f"{numbers}. El más alto fue {max_number}")