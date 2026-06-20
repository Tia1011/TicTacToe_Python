#global variable for a board game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# get user input
def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer 
    else:
        print("Number is invalid or has been filled")

# check for a win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-" :
        winner = board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner = board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-" :
        winner = board[6]

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-" :
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-" :
        winner = board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-" :
        winner = board[2]

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-" :
        winner = board[0]
    elif board[2] == board[4] == board[6] and board[2] != "-" :
        winner = board[2]


# switch the player
def switchPlayer(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"

while gameRunning:
    printBoard(board)
    playerInput(board)
    currentPlayer = switchPlayer(currentPlayer)
    checkDiagonal(board)
    checkHorizontal(board)
    checkVertical(board)
    if winner != None:
        printBoard(board)
        print("Congratulations! Player " + winner + " won.")
        gameRunning = False
        print("= End of Game =")