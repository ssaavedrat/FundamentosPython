# Supongamos que y es un número, por ejemplo:
y = 123.456789

# Aplicamos el formato ".2g"
y_str_g = format(y, ".2g")

# Aplicamos el formato ".2"
y_str_dec = format(y, ".2")

# Imprimimos los resultados
print(y_str_g)    # Salida: 1.2e+02
print(y_str_dec)  # Salida: 123.46