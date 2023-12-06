text = 'Ella sabe programar en Python'
# "in" para verificar pertenencia
print("Python" in text)

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')
'''

size = len(text)
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

# Intercambia mayúsculas con minúsculas
print(text.swapcase())
# Verifica si texto empieza con 'Ella'
print(text.startswith('Ella'))
# Verifica si texto termina con 'Rust'
print(text.endswith('Rust'))
# Si encuentra texto lo reemplaza con Otro
print(text.replace('Python', 'Go'))

# El texto original no cambia
print(text)

text_2 = 'este es un titulo'
print(text_2)
# Primera letra en mayus
print(text_2.capitalize())
# Primera palabra en mayus
print(text_2.title())
# Verifica si string es convertible a digito
print(text_2.isdigit())
print("398".isdigit())
print("398.2349".isdigit())