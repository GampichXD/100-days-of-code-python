# Professional Portfolio Project - Scripting
# Tic Tac Toe Game
# Author : Abraham
# Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_board_full(board):
    return all([cell in ["X", "O"] for row in board for cell in row])


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column: 1 1 for top-left): ")
            row, col = map(int, move.split())
            row -= 1  # convert to 0-indexed
            col -= 1
            if board[row][col] not in ["X", "O"]:
                return row, col
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers from 1 to 3.")


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run the game
tic_tac_toe()
