def display_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print("\n")


def player_input(player, board):
    while True:
        try:
            pos = int(input(f"Player {player}, enter (1-9): ")) - 1
            if pos in range(9) and board[pos] == ' ':
                return pos
            print("Invalid move! Try again.")
        except ValueError:
            print("Enter a number between 1 and 9!")


def check_win(board):

    win_combinations = [
        [0, 4, 8], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8],

    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]


    if ' ' not in board:
        return "Tie"

    return None


def play():
    board, player = [' '] * 9, 'X'
    print("Tic-Tac-Toe! Positions:\n")
    display_board([str(i + 1) for i in range(9)])

    while True:
        display_board(board)
        board[player_input(player, board)] = player
        result = check_win(board)

        if result:
            display_board(board)
            print(f"Game over! {'Tie!' if result == 'Tie' else f'Player {result} wins!'}")
            return play() if input("Play again? (y/n): ").lower() == 'y' else print("Thanks for playing!")

        player = 'O' if player == 'X' else 'X'


if __name__ == "__main__":
    play()
