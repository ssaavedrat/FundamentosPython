# Creación de diccionario
person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print("Diccionario persona:")
print(person)

# Actualizar nombre
person['name'] = 'santi'
# Actualizar edad
person['age'] -= 50
# Agregar un lenguaje a la lista langs
person['langs'].append('rust')

print("Diccionario modificado:")
print(person)

# Eliminar par key-value 'last_name'
del person['last_name']
# Otra forma: eliminar par key-value 'age' con pop que debe ir con un argumento (a dif. de las listas)
person.pop('age')

print('Diccionario despues de eliminar:')
print(person)

print('Items del Diccionario')
# Lista de tuplas (key, value) del diccionario
print(person.items())

print('Keys o Llaves del Diccionario')
print(person.keys())

print('Values o Valores del Diccionario')
print(person.values())
