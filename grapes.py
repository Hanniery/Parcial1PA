if __name__ == '__main__':
  number_to_eat = input()
  andrew, dmitry, michal = int(number_to_eat.split(' ')[0]), int(number_to_eat.split(' ')[1]), int(number_to_eat.split(' ')[2])
  number_to_by_box = input()
  grapes_green, grapes_purple, grapes_black = int(number_to_by_box.split(' ')[0]), int(number_to_by_box.split(' ')[1]), int(number_to_by_box.split(' ')[2])

  bandera = 'YES'

  if andrew <= grapes_green:
    grapes_green -= andrew
  else:
    bandera = 'NO'

  if dmitry > (grapes_green + grapes_purple):
    bandera = 'NO'
  else:
    grapes_green -= dmitry // 2
    grapes_purple -= dmitry // 2

  if michal > (grapes_green + grapes_purple + grapes_black):
    bandera = 'NO'

  print(bandera)