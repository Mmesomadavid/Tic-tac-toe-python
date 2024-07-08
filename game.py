def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the current player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        row = int(input("Enter row number (0, 1, 2): "))
        col = int(input("Enter column number (0, 1, 2): "))
        
        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)
            
            if check_winner(board, player):
                print(f"Player {player} wins!")
                break
            
            if turn == 8:
                print("It's a draw!")
                break
            
            turn += 1
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    main()
