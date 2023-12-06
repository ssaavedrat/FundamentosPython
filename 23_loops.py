# Matriz: lista de listas
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# Accedemos a un elemento con doble indice
print(f'El elemento (fila,columna):(0,1) es {matriz[0][1]}')


# Itera sobre filas
for row in matriz:
  print(row)
  # Itera sobre columnas
  for column in row:
    print(column)