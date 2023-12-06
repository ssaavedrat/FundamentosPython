x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Forma de comparación string
y_str = format(y, ".2g")
print(f'El tipo de dato de y_str es {type(y_str)}')
print('str =>', y_str)
print(y_str == str(x))

print('*' * 10)

# Forma de comparación matemática

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)

