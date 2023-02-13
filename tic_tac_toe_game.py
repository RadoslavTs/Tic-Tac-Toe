from collections import deque
from pyfiglet import Figlet


def check_win(player, symbol):
    first_diagonal_check = all([board[i][i] == symbol for i in range(size)])
    second_diagonal_check = all([board[i][size - 1 - i] == symbol for i in range(size)])
    row_check = any([all(el == symbol for el in row) for row in board])
    column_check = any([all(board[r][c] == symbol for r in range(size)) for c in range(size)])

    if any([first_diagonal_check, second_diagonal_check, row_check, column_check]):
        # print(f"{player} won!")
        winner = Figlet(font='slant')
        print(winner.renderText(f"{player} won!"))
        raise SystemExit


def check_draw():
    if all([all(pos.strip() for pos in row) for row in board]):
        print("Draw!")
        raise SystemExit


def start_the_game():
    player, symbol = players[0]

    player_pick = int(input(f"{player}, choose a free position [1-9]: "))
    if 1 <= player_pick <= size * size:
        col, rol = (player_pick - 1) // size, (player_pick - 1) % size

        if board[col][rol] == " ":
            board[col][rol] = symbol

        else:
            print(f"{player}, this position is occupied, pick an empty position!\n")
            return start_the_game()

    else:
        print(f"{player}, this position is outside the playing board, pick a valid position!\n")
        return start_the_game()

    print_board()

    check_win(player, symbol)

    check_draw()

    players.append(players.popleft())

    start_the_game()


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row_board)} |") for row_board in board]
        for i in range(size):
            for j in range(size):
                board[i][j] = ' '

        print(f"{players[0][0]} starts first!")
        print()
    else:
        [print(f"| {' | '.join(row_board)} |") for row_board in board]
        print()


def get_players():

    while True:
        player_one_name = input("Player one name: ")
        if player_one_name:
            break
        else:
            print("You must pick a name\n")
    while True:
        player_two_name = input("Player two name: ")
        if player_two_name:
            break
        else:
            print("You must pick a name\n")

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with 'X' or 'O'? ").upper()

        if player_one_symbol in ["X", "O"]:
            player_two_symbol = "X" if player_one_symbol == "O" else "O"
            players.append([player_one_name, player_one_symbol])
            players.append([player_two_name, player_two_symbol])
            break

        else:
            print(f"{player_one_name}, please pick a valid symbol!\n")
            continue

    print_board(True)
    start_the_game()


players = deque()
size = 3
board = []
for row in range(1, size * size + 1, 3):
    board.append([str(row), str(row + 1), str(row + 2)])

figlet = Figlet(font="slant")
print(figlet.renderText("Tic - Tac - Toe"))

get_players()
