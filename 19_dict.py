# Diccionarios

# Almacenan clave valor
# Definidos con corchetes {}
my_dict = {}
print(type(my_dict))

# Crear diccionario con elementos
my_dict = {
  'avion': "bla bla bla",
  'name': 'Sergio',
  'last_name': 'Saa',
  'age': 87
}

print("Mi diccionario: ",my_dict)
# El largo del diccionario cuenta el número de pares llave-valor
print("Tamaño de diccionario: ",len(my_dict))

# Llamada de valores
print("Mi nombre es: ",my_dict['name'])
print(my_dict['age'])
print(my_dict['last_name'])

# Es util llamar con get, pues si la llave no existe en el dict retornará None en vez de detener el programa 
print(my_dict.get('age'))

# Verificar si una llave existe en el diccionario
print('avion' in my_dict)
print('otroqueno' in my_dict)

