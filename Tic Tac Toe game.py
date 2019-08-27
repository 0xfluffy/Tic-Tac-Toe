
#This is a Game class makes Tic Tac Toe
class Game:

    #This is a constructor, initializes x to 0 and y to 0 as well as 2Dimmensinal board (2D list)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    #This function prints the board
    def printBoard(self):
        print("     1       2       3")
        print("  -------+-------+-------")
        print("1    "+self.board[0][0]+"   |   "+self.board[1][0]+"   |   "+self.board[2][0])
        print("  -------+-------+-------")
        print("2    "+self.board[0][1]+"   |   "+self.board[1][1]+"   |   "+self.board[2][1])
        print("  -------+-------+-------")
        print("3    "+self.board[0][2]+"   |   "+self.board[1][2]+"   |   "+self.board[2][2])
        print("  -------+-------+-------")

    #This function checks to see if space on the board is empty or not,
    #returns True if empty or False if not empty
    def checkSpace(self, x, y):
        print("Checking if space is empty")
        if self.board[x][y] == 'X' or self.board[x][y] == "0":
            print("Space is not empty! Please select another coordinate!")
            return False
        else:
            print("Space is empty")
            return True

    #This function checks the whole board to see if there is an empty space or not, returns false if empty space and true if space is full (Draw or not)
    def searchWholeBoardForTie(self):
        if " " in self.board[0][0] or " " in self.board[1][0] or " " in self.board[2][0] or " " in self.board[0][1] or " " in self.board[1][1] or " " in self.board[2][1] or " " in self.board[0][2] or " " in self.board[1][2] or " " in self.board[2][2]:
            return False
        else:
            return True


    def checkWinnerX(self):
        #Winner by default is false
        winner = False
        #Horizontal Check for X
        if self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True
        elif self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True
        elif self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True

        #Vertical Check for X
        elif self.board[0][0] == "X" and self.board[0][1] == "X" and self.board[0][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True
        elif self.board[1][0] == "X" and self.board[1][1] == "X" and self.board[1][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True
        elif self.board[2][0] == "X" and self.board[2][1] == "X" and self.board[2][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True

        #Diagonal X
        elif self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True
        elif self.board[2][0] == "X" and self.board[1][1] == "X" and self.board[0][2] == "X":
            self.printBoard()
            print(player1Name+" (X) is the winner")
            winner = True

        return winner


    def checkWinner0(self):
        winner = False
        # Horizontal Check for 0
        if self.board[0][0] == "0" and self.board[1][0] == "0" and self.board[2][0] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        elif self.board[0][1] == "0" and self.board[1][1] == "0" and self.board[2][1] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        elif self.board[0][2] == "0" and self.board[1][2] == "0" and self.board[2][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True

        # Vertical Check for 0
        elif self.board[0][0] == "0" and self.board[0][1] == "0" and self.board[0][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        elif self.board[1][0] == "0" and self.board[1][1] == "0" and self.board[1][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        elif self.board[2][0] == "0" and self.board[2][1] == "0" and self.board[2][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True

        # Diagonal 0
        elif self.board[0][0] == "0" and self.board[1][1] == "0" and self.board[2][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        elif self.board[2][0] == "0" and self.board[1][1] == "0" and self.board[0][2] == "0":
            self.printBoard()
            print(player2Name+" (0) is the winner")
            winner = True
        return winner

    def checkWhosTurn(self):
        #Count is being incremented after each players turn
        #If count modulus 2 gives remainder 0 then its divisble by 2 which means its player 2's turn
        if count % 2 == 0:
            return False
        #Else if remainder then its player 1's turn
        else:
            return True


#This function check to see if X won or 0 won, it will exit clean if X or 0 is the winnder
def winOrLose(game):
    # Check for winner
    winnerX = game.checkWinnerX()
    winner0 = game.checkWinner0()
    if winnerX == True or winner0 == True:
        exit(0)

#This function starts the game
def startGame(game):
    global player1Name
    global player2Name
    global count
    count = 1

    #Welcome Message
    print("##############Welcome to TicTacToe##############")
    #Asks for player names before entering the loop
    player1Name = input("Please enter Player 1's (X) name: ")
    player2Name = input("Please enter Player 2's (0) name: ")

    player1Choice = int()
    player2Choice = int()
    while True:
        #Calls print board
        game.printBoard()

        #Asks the players if they want to put x or 0 or 3 to quit
        #playerChoice = int(input("Please press 1) for X or press 2) for 0 or press 3) to quit: "))
        whosTurn = game.checkWhosTurn()
        if whosTurn == True:
            player1Choice = int(input("Player 1's turn Press 1) to HIT or 3) to quit: "))
        else:
            player2Choice = int(input("Player 2's turn, Press 2 to HIT or 3) to quit: "))


        #Check if player wants to play else quit
        if player1Choice == 3 or player2Choice == 3:
            print("Quitting!")
            exit(0)
        elif player1Choice > 3 or player2Choice > 3:
            print("Error!!!! Please enter a number between 1 to 3")
            continue
        elif player1Choice == 1 or player2Choice == 2:
            # Asks for players x and y coordinates
            playerCoordinateY = int(input("Please enter Y coordinate, a number between 1-3: (Vertical): "))
            playerCoordinateX = int(input("Please enter X coordinate, a number between 1-3: (Horizontal): "))

            #Checks to see if the cordinates entered are empty on the board (Space empty on the board)
            isEmpty = game.checkSpace(playerCoordinateX - 1, playerCoordinateY - 1)
            #If is space is empty then execute the condtion else just continue
            if isEmpty:
                if player1Choice == 1:
                    print("Inserting X on the board")
                    game.board[playerCoordinateX - 1][playerCoordinateY - 1] = "X"
                    #game.board[playerCoordinateY - 1][playerCoordinateX - 1] = "X"
                    player1Choice = 0
                    count += 1
                elif player2Choice == 2:
                    print("Inserting 0 on the board")
                    game.board[playerCoordinateX - 1][playerCoordinateY - 1] = "0"
                    #game.board[playerCoordinateY - 1][playerCoordinateX - 1] = "0"
                    player2Choice = 0
                    count += 1
                else:
                    print("Invalid input please enter X or 0")
                    continue
                winOrLose(game)
                #If there is no winner then checks to see if there is a draw or not by checking " " empty spaces, if draw then exit clean
                isDraw = game.searchWholeBoardForTie()
                if isDraw:
                    game.printBoard()
                    print("DRAW there is no WINNER")
                    exit(0)
            else:
                continue
        else:
            print("Invalid Choice")
            continue
#This here is the main function entry point
def main():
    #Creates a game object
    game = Game()

    #Starts the Game, and passes game object as parameter
    startGame(game)

# Entry Point, calls the main function
if __name__ == '__main__':
    main()