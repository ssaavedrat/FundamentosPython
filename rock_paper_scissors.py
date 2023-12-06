# Librería para datos aleatorios
import random

# Opciones son una tupla (inmutable)
options = ('piedra', 'papel', 'tijera')

# Número de victorias de computadora y usuario
computer_wins = 0
user_wins = 0

# Contador de rondas (inicia en primera ronda)
rounds = 1

while True:

  # Imprimir ronda
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  # Imprimir marcador
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  # Preguntar a usuario jugada
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  # Incrementar la ronda
  rounds += 1

  # Si user_option no está en la tupla...
  if not user_option in options:
    # ... avisar al usuario y reiniciar el ciclo
    print('esa opcion no es valida')
    continue

  # Computadora escoje una opción aleatoria de la tupla options
  computer_option = random.choice(options)

  print('Tu jugada:', user_option)
  print('Jugada de Computadora:', computer_option)

  # Empate
  if user_option == computer_option:
    print('Empate!')

  # Si no es empate, entonces hay un ganador (user o computadora)
  # User 'piedra'
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('¡Tu ganas!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('¡Computadora gana!')
      computer_wins += 1
  # User 'papel'
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('¡Tu ganas!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('¡Computadora gana!')
      computer_wins += 1
  # User 'tijera'
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('¡Tu ganas!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('¡Computadora gana!')
      computer_wins += 1

  if computer_wins == 2:
    print('El Ganador es la Computadora')
    break

  if user_wins == 2:
    print('Eres el Ganador, ¡Felicidades!')
    break
