# For
# Se utiliza con números de elementos o iteraciones predefinidas por algún elemento

# Imprimir 10 números
print(f'Imprimir 10 números')
for i in range(10):
  print(i)

# Imprimir números del 1 al 10
print(f'Imprimir números del 1 al 10')
for i in range(1, 11):
  print(i)

my_list = [23, 45, 67, 89, 43]
print(f'Imprimir números de la lista')
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
# Podemos iterar sobre una tupla
print(f'Imprimir nombres de la tupla')
for element in my_tuple:
  print(element)

product = {'name': 'Camisa', 'price': 100, 'stock': 89}

# Podremos iterar sobre un diccionario
print(f'Imprimir llave y valor del diccionario')
for key in product:
  print(key, ':', product[key])

# Alternativamente podemos iterar sobre dict.values()
for key, value in product.items():
  print(key, ":", value)

people = [{
    'name': 'nico',
    'age': 34
}, {
    'name': 'zule',
    'age': 45
}, {
    'name': 'santi',
    'age': 4
}]

# Iterando sobre una lista de diccionarios
# En este caso una lista de personas (dict)
for person in people:
  # print(person)
  print('Name:', person['name'])
