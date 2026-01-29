def run():  # Запуск игры

    print("Игра запустилась!!!")

def draw_board():  # Создание игрового поля

    print("Создание игрового поля...")


# Тестовая отрисовка пустого игрового поля
a = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
for z, i in enumerate(a):
  for x, y in enumerate(i):
    if x < len(i) - 1:
      print(y + " | ", end = "")
    else:
      print(y, end = "")
  if z < len(a) - 1:
    print()
    print("- - - - -")