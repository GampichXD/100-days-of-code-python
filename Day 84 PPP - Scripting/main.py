# Professional Portfolio Project - Scripting
# Tic Tac Toe Game
# Author : Abraham
placeholder = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
border = ['_' for _ in range(11)]  # Initialize the board with empty spaces
board = f"{' '.join(placeholder)}\n{' '.join(border)}\n\n{' '.join(placeholder)}\n{' '.join(border)}\n\n{' '.join(placeholder)}\n"
print(board)

print(len(board))
