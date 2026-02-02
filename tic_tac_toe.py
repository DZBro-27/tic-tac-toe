def run():  # Запуск игры

    print("Игра запустилась!!!")

def draw_board(board):
    """Отрисовка игрового поля"""
    
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

def create_board(n: int) -> list[list[str]]:
    """Создание игрового поля размером n x n"""
    board = []
    for outer in range(n):
        row = []
        for inner in range(n):
          row.append(" ")
        board.append(row)
    return board
