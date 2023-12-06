# Uso de NOT

# Uso básico
print(not True)
print(not False)

# AND y NOT
print('NOT AND ó NAND')
print('not (True and True) =>', not (True and True))
print('not (True and False) =>', not (True and False))
print('not (False and True) =>', not (False and True))
print('not (False and False) =>', not (False and False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

# Sera verdadero si stock no está entre [100,1000]
print(not (stock >= 100 and stock <= 1000))