print("Хай")
print("Поставь три в ряд, чтобы победить :)")


def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")


def get_input(board, player):
    while True:
        try:
            row = int(input(f"Ход игрока {player} (номер ряда 0-2): "))
            kol = int(input(f"Ход игрока {player} (номер столбца 0-2): "))
            if board[row][kol] == " ":
                return row, kol
            else:
                print("Занято!")
        except ValueError:
            print("Некорректный ввод!")
        except IndexError:
            print("Некорректный ввод!")


def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    else:
        return None


def play_game():
    board = [[" " for i in range(3)] for j in range(3)]
    players = ["X", "0"]
    current = players[0]
    while True:
        print_board(board)
        row, col = get_input(board, current)
        board[row][col] = current
        winner = check_win(board)
        if winner is not None:
            print_board(board)
            print(f"Игрок {winner} выиграл!!!")
            break
        if " " not in [cell for row in board for cell in row]:
            print_board(board)
            print("Ничья(")
            break
        current = players[(players.index(current)+1) % len(players)]


play_game()
