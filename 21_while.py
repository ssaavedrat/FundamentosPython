# While

# Librería time para pausas dramáticas
import time
"""
# Loop Infinito
while True:
  print('se ejecutó')
"""

# Condición inicial
counter = 0

# Ciclo while
while counter < 10:
  counter += 1
  print(counter)
  time.sleep(0.3)

counter = 0
# Rompiendo el ciclo con break
while counter < 20:
  counter += 1
  time.sleep(0.2)
  if counter == 15:
    print('Dejando el ciclo')
    break
  print(counter)

counter = 0
# Saltar a la siguiente iteración del ciclo con continue
while counter < 20:
  counter += 1
  time.sleep(0.1)
  if counter < 15:
    print(f'Soy el número {counter} y soy menor que 15')
    continue
  print(counter)
