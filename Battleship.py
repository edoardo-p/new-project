from random import randint
#creating the board (first number = rows, second number = columns)
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print "You need to sink 3 battleships"
print
#choosing a random row and col for each boat
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
    
def no_repeats(row1, col1, row2, col2):
    while row1 == row2 and col1 == col2:
        row2 = random_row(board)
        col2 = random_col(board)

ship_row1 = random_row(board)
ship_col1 = random_col(board)

ship_row2 = random_row(board)
ship_col2 = random_col(board)

ship_row3 = random_row(board)
ship_col3 = random_col(board)

no_repeats(ship_row1, ship_col1, ship_row2, ship_col2)
no_repeats(ship_row2, ship_col2, ship_row3, ship_col3)

turn = 0
#for loop which makes sure every possible outcome of guess_row and guess_col is covered
for turn in range(15):
    print "Turn", turn + 1
    guess_row = input("Guess Row: ") - 1
    guess_col = input("Guess Col: ") - 1
    print
    #winning scenarios (one boat is sunk)
    if guess_row == ship_row1 and guess_col == ship_col1:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "0"
        print_board(board)
    elif guess_row == ship_row2 and guess_col == ship_col2:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "0"
        print_board(board)
    elif guess_row == ship_row3 and guess_col == ship_col3:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "0"
        print_board(board)
    else:
        #user inputs are bigger than the board
        if (guess_row < 0 or guess_row > (len(board) - 1)) or \
           (guess_col < 0 or guess_col > (len(board) - 1)):
            print "Oops, that's not even in the ocean."
            print_board(board)
        elif(board[guess_row][guess_col] == "X") or \
            (board[guess_row][guess_col] == "0"):
            print "You guessed that one already."
            print_board(board)
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    #executes when all ships are sunk
    print
    if board[ship_row1][ship_col1] == "0" and \
       board[ship_row2][ship_col2] == "0" and \
       board[ship_row3][ship_col3] == "0":
        print "You Won! Hoorah!"
            
    #executes after you lose, prints ships' positions
    if turn == 14:
        print "Game Over"
        print "The battleships were at:"
        print "(%s, %s)" %(ship_row1 + 1, ship_col1 + 1)
        print "(%s, %s)" %(ship_row2 + 1, ship_col2 + 1)
        print "(%s, %s)" %(ship_row3 + 1, ship_col3 + 1)
