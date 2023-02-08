# Basic Tic-Tac-Toe Game

from collections import deque


def create_board():
    board = []

    for i in range(1, 10, 3):
        board.append([str(i), str(i+1), str(i+2)])

    return board


def setup_players_names_and_symbols():

    def first_player_symbol_pick():
        first_player_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

        if first_player_symbol not in ["X", "O"]:
            print("You can only chose between 'X' and 'O', please try again to pick your symbol!")
            first_player_symbol = first_player_symbol_pick()

        return first_player_symbol

    player_one_name = input("First player's name: ")
    player_two_name = input("Second player's name: ")
    player_one_symbol = first_player_symbol_pick()
    player_two_symbol = "X" if player_one_symbol == "O" else "O"
    players = deque()
    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    return players


def implement_choice(board, player_choice, players):
    row, col = (player_choice - 1) // 3, (player_choice - 1) % 3

    if board[row][col] == " ":
        board[row][col] = players[0][1]

    else:
        print(f"Ooops {players[0][0]}, looks like the desired position is already taken. "
              f"Please try with a different one!!!")
        board, players = current_player_choice(players, board)

    return board, players


def current_player_choice(players, board):
    try:
        player_choice = int(input(f"{players[0][0]} chose a free position [1-9]: "))
        board, players = implement_choice(board, player_choice, players)
    except IndexError:
        print("It looks like you entered an invalid position. Please enter a valid position [1-9].")
        board, players = current_player_choice(players, board)

    return board, players


def print_board_func(board, players, begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first")

        for row in range(3):
            for col in range(3):
                board[row][col] = " "

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def check_for_win(board, players):

    first_diagonal = all(board[i][i] == players[0][1] for i in range(3))
    second_diagonal = all(board[i][3 - 1 - i] == players[0][1] for i in range(3))
    horizontal = any(all(board[row][col] == players[0][1] for col in range(3)) for row in range(3))
    vertical = any(all(board[row][col] == players[0][1] for row in range(3)) for col in range(3))

    return any([first_diagonal, second_diagonal, horizontal, vertical])


def check_for_draw(board):
    return all([all(el.strip() for el in row) for row in board])


def play(players, board):
    while True:
        board, players = current_player_choice(players, board)
        print_board_func(board, players)
        if check_for_win(board, players):
            print(f"{players[0][0]} won the game!!!")
            break
        elif check_for_draw(board):
            print("Draw!!! The game finished without a winner!")
            break
        players.append(players.popleft())


def setup():
    board = create_board()
    players = setup_players_names_and_symbols()
    print_board_func(board, players, begin=True)
    play(players, board)


setup()
