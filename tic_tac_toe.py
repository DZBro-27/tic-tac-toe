def run():  # Запуск игры

    print("Игра запустилась!!!")

def create_board(n: int) -> list[list[str]]:
    """Создание игрового поля размером n x n"""
    board = []
    for outer in range(n):
        row = []
        for inner in range(n):
          row.append(" ")
        board.append(row)
    return board
