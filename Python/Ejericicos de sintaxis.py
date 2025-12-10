import random

#1. Experimiento con sumas (la idea de este ejercicio era expermientar y ver que tipo de errores tira, los cuales puse en comentarios)

print("Ejericio 1: ---------------------------------------------")
string_sum = "1" + "1"
#string_int_sum = "1" + 1 can only concatenate str (not "int") to str -> este error lo tira porque piensa que se va hacer una concatenacion de otro string y no espera un numero
#int_string_sum = 1 + "1" unsupported operand type(s) for +: 'int' and 'str' -> al contrario del anteior este se da porque pinesa que se a hacer una suma de dos numero pero se presenta un string en ves de un numero
list_list_sum = [1, 2, 3] + [4, 5, 6]
#string_list_sum = "hello world" + [1, 2, 3] #can only concatenate str -> espera la concatenaicon de 2 strings 
float_int_sum = 3.5 + 1
bool_bool_sum = True + True #Esto arroja un 2 ya que el True se interpreta como 1 por debajo

print(string_sum)

for number in list_list_sum:
    print(number)

print(float_int_sum)
print(bool_bool_sum)



print("Ejericio 2: ---------------------------------------------")

name = input("Ingrese su nombre completo: ")
age = float(input("Ingrese su edad: "))

if(age > 0 and age < 2):
    print(f"{name} eres un bebé")

elif(age >= 2 and age <= 10):
    print(f"{name} eres un niño")

elif(age > 10 and age <= 12):
    print(f"{name} eres un preadolescente")

elif(age > 12 and age < 18):
    print(f"{name} eres un adolescente")

elif(age >= 18 and age < 40):
    print(f"{name} eres un adulto joven")

elif(age >= 40 and age < 65):
    print(f"{name} eres un adulto")

elif(age >= 65):
    print(f"{name} eres un adulto mayor")

else:
    print("valor inválido")

print("Ejericio 3: ---------------------------------------------")

random_int = random.randint(0, 10)
user_value = -1

while(user_value != random_int):
    user_value = int(input("Adivine un numero del 0 al 10: "))

    if(user_value == random_int):
        print("Adivinaste :)")
    
    else:
        print("Incorrecto :(")

print("Ejericio 4: ---------------------------------------------")

grater_number = 0
for i in range(1, 4):
    user_value_exercise4 = int(input(f"Ingrese el número {i}: "))        

    if(user_value_exercise4 > grater_number):
        grater_number = user_value_exercise4

print(f"El numero mayor es: {grater_number}")

print("Ejericio 5: ---------------------------------------------")

user_input = input("Ingrese las notas que desea calcular separada unicamente por comas y sin espacios (50,90,100,75):")
scores = [int(num) for num in user_input.split(',')]
approved = 0
disapproved = 0
scores_sum = 0
score_approved_sum = 0
score_disapproved_sum = 0

for score in scores:
    if(score >= 70):
        approved += 1
        score_approved_sum = score_approved_sum + score
    else:
        disapproved += 1
        score_disapproved_sum = score_disapproved_sum + score
    
    scores_sum = scores_sum + score

score_average = scores_sum / len(scores)
score_approved_average = score_approved_sum / approved
score_disapproved_average = score_disapproved_sum / disapproved

print(f"Notas aprovadas: {approved}")
print(f"Notas desaprovadas: {disapproved}")
print(f"El promedio de las notas es: {score_average}")
print(f"El promedio de las notas aprovadas es: {score_approved_average}")
print(f"El promedio de las notas desaprovadas es: {score_disapproved_average}")
