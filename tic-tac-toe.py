import os

#function clears terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#displays tic-tac-toe board
def show(b):
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")

#function determines winner
def winner(b):

    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, c, d in wins:
        if b[a] == b[c] == b[d]:
            return b[a]
    return None

#function plays the game
def play():
    b = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in b):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(b)
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and b[move].isdigit():
            b[move] = turn
            winner_result = winner(b)
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(b)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(b)
    print("\nIt's a draw!")

play()
