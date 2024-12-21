import random


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Check if a move is valid
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


# Get player input
def player_input(board, player):
    while True:
        try:
            row, col = map(int, input(
                f"Player {player}, enter your move (row and column, 1-3): ").split())
            row, col = row - 1, col - 1  # Convert to zero-based index
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move!"
                      " The cell is already taken or out of bounds.")
        except ValueError:
            print("Invalid input!"
                  " Enter row and column numbers between 1 and 3.")


# AI's move
def ai_move(board):
    # Simple AI: Picks the first available cell
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col


# Update the board with the player's move
def update_board(board, row, col, player):
    board[row][col] = player


# Check for a win
def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if (all(board[i][j] == player for j in range(3)) or
                all(board[j][i] == player for j in range(3))):
            return True
    # Check diagonals
    if (all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3))):
        return True
    return False


# Check for a tie
def check_tie(board):
    return all(cell != " " for row in board for cell in row)


# Main game loop
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    mode = input("Choose game mode: 1 for Human vs Human,"
                 " 2 for Human vs AI: ").strip()

    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)

        if mode == "2" and current_player == "O":
            print("AI is making its move...")
            row, col = ai_move(board)
        else:
            row, col = player_input(board, current_player)

        update_board(board, row, col, current_player)

        # Check for win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()