# CRUD Create, Read, Update & Delete

# Crear
numbers = [1, 2 , 3 , 4 , 5]
# Leer
print(numbers[1])
# Actualizar (update value)
numbers[-1] = 10
print(numbers)

# Actualizar (new value)
numbers.append(700)
print(numbers)

# Insertar en un lugar específico de la lista
numbers.insert(0, 'hola')
print(numbers)

# Insertar en la posición 3
numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
# Suma de listas
new_list = numbers + tasks
print(new_list)

# Obtener el índice de un elemento
index = new_list.index('todo 2')
print(f'El índice del elemento es {index}')
new_list[index] = 'todo changed'
print(new_list)

# Delete
new_list.remove('todo 1')
print(new_list)

# Eliminar ultimo elemento de lista
print('pop()')
new_list.pop()
print(new_list)

# Eliminar una posición
print('pop(0)')
new_list.pop(0)
print(new_list)

# Revertir el orden de la lista
new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6 , 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

print(new_list)
# Sort no funciona con tipos mezclados
# new_list.sort()