"""
Pseudocode: 

1. create a grid 
2. prompt the first player for their move
3. put the symbol into the board at the appropriate space 
    (for this - maybe do 1 2 3 / 4 5 6 / 7 8 9 printed out)
4. check to see if any end game conclusions have been hit
5. if yes check and announce winner; if no, keep playing

"""


def playGame():
    """
    Contains main game logic. 
    1. asks for p1 and p2's names
    2. prints instructions as to who is what move
    3. displays the board
    4. while the game is still playable, prompts users for a move. each move, the board is checked for end game condition
    5. if the game has ended, print results. if the game has not ended, continue to play
    """
    # initialize the game array
    arr = initializeGame()

    # get names
    p1name = input("What is player 1's name? ")
    p2name = input("What is player 2's name? ")

    # instruct players
    print("{} is o. {} is x.".format(p1name, p2name))

    # display board
    printBoard(arr)

    # move handling - first move is "o". this will update to flip back and forth between moves.
    move = "o"
    name = p1name

    gameon = True

    # continue to run this loop until there are no more available moves
    while gameon == True:
        # player turn
        arr = getMove(arr, move, name)

        # Check end condition. if the game has ended, set gameon to false and print results.
        res = checkEnd(arr)

        if res[0] == True:
            gameon = False
            if res[1] == "TIE":
                print("Game over! Tie!")
            elif res[1] == "o":
                print("Game over! {} has won!".format(p1name))
            else:
                print("Game over! {} has won!".format(p2name))
        else:
            if move == "o":
                move = "x"
                name = p2name
            else:
                move = "o"
                name = p1name
        printBoard(arr)


def initializeGame():
    """
    Creates the initial blank array
    """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def printBoard(arr):
    """
    Print out the tic tac toe board, based on an input array. This will update as the board is filled out.
    """
    line = "|"
    for index, item in enumerate(arr):
        if index == 2 or index == 5:
            line = line + ("_{}_|".format(item)) + "\n"
        elif index == 3 or index == 6:
            line = line + ("|_{}_|".format(item))
        else:
            line = line + ("_{}_|".format(item))

    print(line)


def getMove(arr, side, name):
    """
    Inputs: array of moves left/taken, what character is playing
    Returns: updated array

    Prompts the user where they want to put their mark. Once
    a location has been chosen, update with X or O, depending
    on the player. Update the array.
    """
    move = input("{}, where would you like to put your letter? ".format(name))

    loc = int(move) - 1

    if arr[loc] == "x" or arr[loc] == "o":
        print("There's something there already!")
        getMove(arr, side, name)
    else:
        print("Okay!")
        arr[loc] = side

    return arr


def checkEnd(arr):
    """
    Inputs: array of moves left/taken
    Returns: tuple of two values -- 
      TRUE/FALSE for end of game condition
      winner, or text ("tie" or "continue")

    Checks the game board array to see whether or not
    a win condition has happened, or if the board is 
    out of moves.
    """
    # true/false

    # check to see if any numbers are left
    numleft = False
    for item in arr:
        if item != "x" and item != "o":
            numleft = True

    # return a tuple: the first point will be t/f and the second will be value

    # first - check to see if there is a 3 in a row
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return (True, arr[0])
    elif arr[3] == arr[4] and arr[4] == arr[5]:
        return (True, arr[3])
    elif arr[6] == arr[7] and arr[7] == arr[8]:
        return (True, arr[6])

    # next - 3 up and down
    elif arr[0] == arr[3] and arr[3] == arr[6]:
        return (True, arr[0])
    elif arr[1] == arr[4] and arr[4] == arr[7]:
        return (True, arr[1])
    elif arr[2] == arr[5] and arr[5] == arr[8]:
        return (True, arr[2])

    # last - diagonal
    elif arr[0] == arr[4] and arr[4] == arr[8]:
        return (True, arr[4])
    elif arr[2] == arr[4] and arr[4] == arr[6]:
        return (True, arr[4])

    # if no win condition, but no moves left: game is over, no winner
    elif numleft == False:
        return (True, "TIE")

    else:
        return (False, "continue!")


playGame()
