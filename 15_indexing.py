text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])
size = len(text)
print('El largo de la palabra es:',size)
print(text[15])
print(text[size - 1])
# Nos podemos "ahorrar" size
print(text[-1])

# Slicing

# Posición cero a posición 4
print(text[0:5])
# Posición 10 a posición 15
print(text[10:16])
# Selecciona los primeros 9 caracteres
print(text[:10])
# Selecciona de la posición 5 a la penúltima
print(text[5:-1])
# Selecciona de la posición 5 hasta el final
print(text[5:])
# Selecciona todo el texto
print(text[:])

# Slicing con salto simple
print(text[10:16:1])
# Slicing con salto doble
print(text[10:16:2])
# Salto de dos en dos
print(text[::2])

# Invertir el texto
print(text[::-1])