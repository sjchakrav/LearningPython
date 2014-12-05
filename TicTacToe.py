#first create the board for the game to be played on
def print_board(): #use two for loops go through the variable print_board, the 2 dimensional list
    for i in range(0,3): #the board will be 3x3 indicated by the range
        for x in range(0,3):
            print board[2-i][x], #the 2-i is used to inverse the value of the boards so that the lowest numbers (1,2,3) are listed at the bottom of the board instead of at the top
            if x != 2: # this condition is needed to ensure the | prints after each square and not every line
                    print " | ",
        print " "

def check_game_over(): #use this function to determine whether or not the game is game_over, if it's over we return as true and print the message out
    for i in range(0,3): #check to see if the value in the squares are the same for the vertical and horizontal lines, range (0,3), #the \ continues the line of code into the next          
        if board[i][0] == board[i][1] == board[i][2] != " " \
        or board[0][i] == board[1][i] == board[2][i] != " ":
            print "\n"
            print turn, "wins!"
            return True
         #check to see if the diagonal lines on the board are holding the same values, return "wins!" if there is a winning line
    if board[0][0] == board[1][1] == board[2][2] != " " \
    or board[0][2] == board[1][1] == board[2][0] != " ":
        print "\n"
        print turn, "wins!"
        return True
        #set the condition for when the individuals are in a draw
#if none of the squares is equal to " " and no one has won, it is a draw

    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print "\n"
        print "Tie!"
        return True
        
  #return false if none of the above is true since the game is not game_over yet  
    return False


#declare the game variables
turn = "X"
board = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
game_over = False #as long as this remains false, the program will keep looping

   #declare a while loop which will continue until game_over = true
while game_over != True:
    print_board()
    print "\n"
    print turn, "'s turn to move"
    print

    not_done = False 
    while not_done != True:
         #print the board so players know which numbers correspond to which
        print "Please select a position corresponding to the numbers below to play (valid numbers are 1-9):"
        print "\n"
        print "7 | 8 | 9"
        print "4 | 5 | 6"
        print "1 | 2 | 3"
        print

        try: #create a condition for the position to be a number 1-9
            pos = input("Select a position: ")
            print "\n"
            if pos <=9 and pos >=1: #the condition that checks that number entered is between the bounds of 1-9
                #we then get the x and y value from the player and see if the position they chose is empty
                #the /3 and %3 correspond to the positions on the board for the x and y positions. Y would correspond to 0,1,2,3 and X would correspond to 0,1,2,
                Y = pos / 3 
                X = pos % 3
                if X != 0:  
                    X -= 1
                else:
                     X = 2
                     Y -= 1
                    
                if board[Y][X] == " ": 
                    board[Y][X] = turn #store the players as X or O
                    not_done = True
                    game_over = check_game_over() #check to see if the game is over
                    #this condition checks to see whose turn it is next if the game is not over
                    if game_over == False:
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"
                
        except:#add the condition to prompt the user for a valid number
            print "You need to add a position corresponding to the valid numbers (1-9) to continue playing:"
