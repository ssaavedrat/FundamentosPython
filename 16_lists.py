# Lista
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

# Otra lista
tasks = ['make a dishes', 'play videogames']
print(tasks)

# Las listas pueden almacenar diferentes tipos de datos
types = [1, True, 'hola']
print(types)

# Seleccionar elementos de listas
print(numbers[0])
print(tasks[0])

text = 'Hola'
# Esto dará error porque los string no son mutables, como las listas
# text[0] = 'W'

# Redefinir elementos de lista
tasks[0] = 'watch platzi courses'
print(tasks)
tasks[0] = 'do the dishes'
print(tasks)

# Slicing en listas
print(numbers[:3])
# Operador in en listas
print(True in types)
print('hola' in types)