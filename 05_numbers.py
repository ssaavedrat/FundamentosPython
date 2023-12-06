# int
lives = 3
print(type(lives))
age = 12
budget = 100

# float
temperature = 12.12
print(type(temperature))

# actualizar variable
lives = 2
print(lives)
lives = 1
print(lives)

# redefinir variable
lives = 12 + 15
print(lives)

# agregar o restar valores a la variable
lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

# Los numeros grandes se representan con notación cientifica
number = 4500000000000000000.1
print(number)

# Al igual que los pequeños
number_b = 0.0000000000000001
print(number_b)

# Obtenemos los presupuestos
budget_1 = input('Presupuesto Enero: ')
budget_2 = input('Presupuesto Febrero: ')
budget_3 = input('Presupuesto Marzo: ')

# Transformando a Int
budget_1 = int(budget_1)
budget_2 = int(budget_2)
budget_3 = int(budget_3)

# Promedio
average = (budget_1 + budget_2 + budget_3) / 3
print(f'El presupuesto promedio es {average}')