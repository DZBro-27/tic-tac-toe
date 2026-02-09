"""Модуль для игры в крестики-нолики."""

def create_board(n: int) -> list[list[str]]:
    """Создание игрового поля размером n x n."""

    board = []
    for outer in range(n):
        row = []
        for inner in range(n):
          row.append(" ")
        board.append(row)
    return board

def draw_board(board):
    """Отрисовка игрового поля."""
    
    # Определяем длину строки игрового поля
    board_size = len(board)
    row_length = 4*board_size - 3  

    # Внешний цикл проходит по строкам игрового поля
    for row_index, row in enumerate(board):
      
      # Внутренний цикл проходит по ячейкам строки
      for col_index, cell in enumerate(row):
        if col_index < len(row) - 1:
          print(cell + " | ", end = "")
        else:
          print(cell, end = "")
          
      if row_index < (board_size- 1):
        print()
        print("-" * row_length)
      else:
        print()

def get_move(board):
  """Получение хода игрока."""
  size = len(board)

  while True:
    move = input(f"Введите координаты хода (номер строки и столбца) через пробел от 1 до {size}: ")
    
    if len(move.split()) != 2:
      print("Введите ДВА числа.")
      continue

    try:
      # Преобразование введенных координат в индексы списка
      row = int(move.split()[0]) - 1
      col = int(move.split()[1]) - 1

    except (ValueError, IndexError):
      print("Неверно указаны координаты.")
      continue

    if not (0 <= row < size and 0 <= col < size):
      print("Неверно указаны координаты.")
      continue

    if board[row][col] != " ":
      print("Клетка занята!")
      continue

    else:
      return row, col

def switch_player(current_player: str):
  """Смена текущего игрока."""
  
  if current_player == "X":
    return "O"

  else:
    return "X"

def make_move(board, row, col, current_player):
  """Выполнение хода игрока."""
  board[row][col] = current_player
  
def check_win(board, current_player):
  """Проверка победы"""

  # Проверка победного условия по строке  
  for row in board:
    is_row_win = True

    for cell in row:

      if cell != current_player:
        is_row_win = False
        break

    if is_row_win == True:
      return True

  
  # Проверка победного условия по столбцу
  size = len(board)

  for col_index in range(size):
    is_col_win = True

    for row_index in range(size):

      if board[row_index][col_index] != current_player:
        is_col_win = False
        break

    if is_col_win:
      return True
    
  # Проверка победного условия по диагонали


def run():
    """Запускает основной игровой цикл."""

    board_size = 3
    board = create_board(3)
    current_player = "X"

    #while True:
    draw_board(board)
    print("\n" f"Ходит игрок {current_player}")
    row, col = get_move(board)
    make_move(board, row, col, current_player)
    draw_board(board)

