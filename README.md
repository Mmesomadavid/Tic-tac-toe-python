# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game implemented in Python. The game allows two players to take turns and play Tic-Tac-Toe in the console.

## How to Play

1. The game is played on a 3x3 grid.
2. Players take turns to enter their moves.
3. On each turn, a player enters the row and column number where they want to place their marker (either 'X' or 'O').
4. The game checks for a win or a draw after each move.
5. The game ends when a player wins or it's a draw.

## Rules

- A player wins if they manage to place three of their markers in a horizontal, vertical, or diagonal row.
- The game ends in a draw if all cells are filled and no player has won.

## Prerequisites

- Python 3.x

## How to Run

1. Clone the repository or download the `tic_tac_toe.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `tic_tac_toe.py` file.
4. Run the game with the command:

    ```sh
    python tic_tac_toe.py
    ```

5. Follow the on-screen instructions to play the game.

## Code Overview

### Functions

- `print_board(board)`: Prints the current state of the Tic-Tac-Toe board.
- `check_winner(board, player)`: Checks if the specified player has won based on the current board state.
- `main()`: The main game loop where players take turns entering their moves until a win or draw condition is met.

### Example

Here's an example of how the game looks in the console:

