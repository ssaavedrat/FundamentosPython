# Tuplas
# Las tuplas son tipos de datos inmutables

# Tupla de números
numbers = (1, 2, 3, 5)
# Tupla de strings
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print(f'El tipo de dato es: {type(numbers)}')

# Puedo indexar elementos
print('numbers[0]: ', numbers[0])
print('numbers[-1]: ', numbers[-1])

print(strings)
print(type(strings))

# CRUD
# Create OK
# Read OK

# Update NO
# numbers.append(10) generará error
# numbers[1] = 'change' generará error
print(numbers)

# Delete NO
# numbers.pop() generará error

print(strings)
# Leer posición
print(strings.index('zule'))
# Contar ocurrencia de elemento en tupla
print(strings.count('nico'))

# Podemos transformar una tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))

# ...cambiar la lista...
my_list[1] = 'juli'
print(my_list)

# ...y "guardar" como una nueva tupla
my_tuple = tuple(my_list)
print(my_tuple)