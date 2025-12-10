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

score_approved_average = 0
if(approved > 0):
    score_approved_average = score_approved_sum / approved

score_disapproved_average = 0
if(disapproved > 0):
    score_disapproved_average = score_disapproved_sum / disapproved

print(f"Notas aprovadas: {approved}")
print(f"Notas desaprovadas: {disapproved}")
print(f"El promedio de las notas es: {score_average}")
print(f"El promedio de las notas aprovadas es: {score_approved_average}")
print(f"El promedio de las notas desaprovadas es: {score_disapproved_average}")
