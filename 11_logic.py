# Operadores Lógicos

# AND
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

# Utilizando comparadores
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

# Uso: Consulta si valor está entre [100, 1000]
stock = input('Ingrese el numero de stock => ')
stock = int(stock)
print(stock >= 100 and stock <= 1000)

# OR
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

# Uso: verificar rol admin o seller
role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')