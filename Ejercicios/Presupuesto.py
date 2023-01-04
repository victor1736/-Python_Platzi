n=0
budget_January = input("Cual es el Presupuesto para el mes de Enero: ")
n+=1
budget_february = input("Cual es el Presuspuesto para el mes de Febrero: ")
n+=1
budget_march = input("Cual es el presupuesto de el mes de marzo: ")
n+=1

total_budget=int(budget_January)+int(budget_february)+int(budget_march)

print("El promedio total de  esos meses fue de: ",total_budget/n)
