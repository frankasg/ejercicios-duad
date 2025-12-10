#Ejercicio 1
print("Ejericio 1: ---------------------------------------------")

hotel = {
    "name": "Riu",
    "stars": 5,
    "rooms": [
        {
            "number": 1,
            "floor": 1,
            "price": 100
        },
        {
            "number": 2,
            "floor": 1,
            "price": 150
        }
    ]
}

#Output Example
print(hotel["rooms"][0]["price"])

#Ejercicio 2
print("Ejericio 2: ---------------------------------------------")

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
result = {}

for index in range(len(list_a)):
    result[list_a[index]] = list_b[index]

print(result)

#Ejercicio 3
print("Ejericio 3: ---------------------------------------------")

list_of_keys  = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for item in list_of_keys:
    employee.pop(item)

print(employee)