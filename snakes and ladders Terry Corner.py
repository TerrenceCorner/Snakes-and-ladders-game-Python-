from turtle import Screen, Turtle #Importing turtle graphics
import turtle

import time

import random 

player_two_score = 0
player_one_score = 0            #Setting out the base values for the game
player_one_name = "name_one"
player_two_name = "name_two"

reset = False  #Sets the reset variable to false to allow the program to create the board on start-up


                                                                       #Array to store the coordinates of each square

index_array = [[turtle.Vec2D(-240.10,-239.90), turtle.Vec2D(-240.10,-119.90), turtle.Vec2D(-240.10,0.10), turtle.Vec2D(-240.10,120.10), turtle.Vec2D(-240.10,240.10)], \
               [turtle.Vec2D(-120.10,-239.90), turtle.Vec2D(-120.10,-119.90), turtle.Vec2D(-120.10,0.10), turtle.Vec2D(-120.10,120.10), turtle.Vec2D(-120.10,240.10)], \
               [turtle.Vec2D(-0.10,-239.90), turtle.Vec2D(-0.10,-119.90), turtle.Vec2D(-0.10,0.10), turtle.Vec2D(-0.10,120.10), turtle.Vec2D(-0.10,240.10)], \
               [turtle.Vec2D(119.90,-239.90), turtle.Vec2D(119.90,-119.90), turtle.Vec2D(119.90,0.10), turtle.Vec2D(119.90,120.10), turtle.Vec2D(119.90,240.10)], \
               [turtle.Vec2D(239.90,-239.90), turtle.Vec2D(239.90,-119.90), turtle.Vec2D(239.90,0.10), turtle.Vec2D(239.90,120.10), turtle.Vec2D(239.90,240.10)]] 

object_positions = {"[0][3]": -360, "[2][1]": -120, "[3][4]": -240, "[1][1]": 120, "[4][0]": 240, "[2][3]": 120}    #Setting the board positions and size of each of the snakes and ladders
                                                                       
#Function to return the coordinates of a position on the game board
#--------------------------------------------------
def get_coordinate (position_column, position_row):
   
    coordinate = index_array[position_column][position_row] #Returns the coordinates of the square requested from the array they are stored in
    return coordinate
   
#Function to create numbers for each square on the game board
#--------------------------------------------------
def draw_numbers():

    number_store = [1, 10, 11, 20, 21, 2, 9, 12, 19, 22, 3, 8, 13, 18, 23, 4, 7, 14, 17, 24, 5, 6, 15, 16, 25] #Sets the order of the numbers to be placed on the board

    count = 0
    column = 0 
    square = 0

    draw_number = Turtle()
    draw_number.hideturtle()
    
    text_font = ("Courier", 20, "bold")   #Sets the details of the numbers to be drawn on the board 

    draw_number.speed(0)
    
    while column < 5:       #Loops through each column on the game board

        while square < 5:   #Loops through all of the squares in that column
            
            coordinate = index_array[column][square] #Obtains the coordinate for each square on the board

            draw_number.penup()
            draw_number.goto(coordinate - (55, -30))     #Moves the turtle to the top left corner of each square to write its number   
            draw_number.pendown()
            draw_number.write(str(number_store[count]), font = text_font)          

            count = count + 1     #Increments through the whole array containing the numbers to write for each square                                               

            square = square + 1   #Increments each square upwards in each column

        column = column + 1     #Increments through each column 

        square = 0      #Resets to the bottom square when a new column is reached     

#Function to create each row of the game board 
#--------------------------------------------------
def draw_row(board, initial):
    
    for i in range(6):
        board.penup()
        board.goto(initial)  #Adds a line for each row of the game board
        board.pendown()
        board.forward(600)
        initial = initial + (0, 120) 
            
#Function to create each column of the game board 
#--------------------------------------------------
def draw_column(board, initial):

    board.left(90)
    
    for i in range(6):
        board.penup()
        board.goto(initial)  #Adds a line for each column of the game board
        board.pendown()
        
        board.forward(600)
        initial = initial + (120, 0)

#Function to create the snakes and ladders on the game board
#--------------------------------------------------
def draw_objects():
    
    screen = Screen()
    
    screen.addshape(name="snake.gif", shape=None)     
    screen.addshape(name="snake2.gif", shape=None)    #Adds the different snake images to the bank of shapes
    screen.addshape(name="snake3.gif", shape=None)

    snake = Turtle()
    snake2 = Turtle()
    snake3 = Turtle()       #Assigns a turtle to each snake image
    snake.penup()
    snake2.penup()
    snake3.penup()

    screen = Screen()
    screen.addshape(name="ladder.gif", shape=None) 
    screen.addshape(name="ladder2.gif", shape=None)  #Adds the different ladder images to the bank of shapes
    screen.addshape(name="ladder3.gif", shape=None)

    count = 0   #Counts up to allow a different turtle to be selected for two same sized ladders in different positions
    
    ladder = Turtle()
    ladder2 = Turtle()
    ladder3 = Turtle()       #Assigns a turtle to each ladder image
    ladder.penup()
    ladder2.penup()
    ladder3.penup()

    for i in object_positions.items():
        reference, size = i
        position_column = int(reference[1:2])       #Loops through the array of snakes/ladders and obtains each's size and coordinates
        position_row = int(reference[4:5])
        coordinate = get_coordinate(position_column, position_row) 
        
        if size == -120:
            snake2.shape("snake2.gif")
            snake2.goto(coordinate - (0, 60))
            
        if size == -240:
            snake.shape("snake.gif")                
            snake.goto(coordinate - (0, 120))       #Checks the size of each snake and offsets it appropriately so it appears in the correct position, across the correct squares
        
        if size == -360:
            snake3.shape("snake3.gif")
            snake3.goto(coordinate - (0, 180))

        if size == 240:
            ladder3.shape("ladder3.gif")
            ladder3.goto(coordinate + (0, 120))
        if size == 120:
            if count == 0:
                ladder.shape("ladder.gif")
                ladder.goto(coordinate + (0, 60))       #Checks the size of each ladder and offsets it appropriately so it appears in the correct position, across the correct squares

            if count == 1:
                ladder2.shape("ladder2.gif")
                ladder2.goto(coordinate + (0, 60))

            count = count + 1

#Function to create the game board
#--------------------------------------------------
def draw_board():
    
    board = Turtle()
    board.hideturtle()
    board.width(3)              #Sets the details for the design of the game board
    turtle.bgcolor("#FFF300")          
    board.speed(0)
    
    initial = turtle.Vec2D(-300, -300) #Setting up the initial position of the turtle creating the board
    
    draw_row(board, initial)    
    draw_column(board, initial)   #Calling the functions to create the grid of the board
    
    draw_numbers()  #Calling the function to draw the number of each square on the board
    
    draw_objects()  #Calling the function to draw the snakes and ladders on the board
    
#Function to add the game pieces to the board
#--------------------------------------------------
def add_pieces():
    
    screen = Screen()

    coordinate = get_coordinate(0, 0)   #Obtains the start coordinates for the game pieces 

    player_one = Turtle()
    player_two = Turtle()    #Assigns a turtle for each player
    player_one.penup()
    player_two.penup()

    screen.addshape(name="bull.gif", shape=None)
    screen.addshape(name="cow.gif", shape=None)     #Adds the images of the game pieces to the bank of shapes

    player_one.shape("bull.gif")                       
    player_one.goto(coordinate - (30, 0))                                 
    player_two.shape("cow.gif")              #Assigns the images for each player's piece to their respective turtle     
    player_two.goto(coordinate + (30, 0))

    return player_one, player_two  #Returns the turtle for each player

#Function to roll the die and display its value
#--------------------------------------------------
def roll_dice(won):

    screen = Screen()
    screen.addshape(name="dice1.gif", shape=None) 
    screen.addshape(name="dice2.gif", shape=None)
    screen.addshape(name="dice3.gif", shape=None)
    screen.addshape(name="dice4.gif", shape=None)     #Adds the images of each side of the die to the bank of shapes
    screen.addshape(name="dice5.gif", shape=None)
    screen.addshape(name="dice6.gif", shape=None)

    dice = Turtle()

    if won:
        dice.hideturtle()    #Removes the image of the die from the previous game when a new game is started
        
    else:
        dice_result = random.randint(1, 6)     #Generates a random number between 1 and 6 to simulate the sides of a die
        dice.penup()                              
        
        if dice_result == 1:
            dice.shape("dice1.gif")
            dice.goto(-375, 0)
        if dice_result == 2:
            dice.shape("dice2.gif")
            dice.goto(-375, 0)
        if dice_result == 3:
            dice.shape("dice3.gif")     #Chooses what side of the die to display based upon the random number generated
            dice.goto(-375, 0)
        if dice_result == 4:
            dice.shape("dice4.gif")
            dice.goto(-375, 0)
        if dice_result == 5:
            dice.shape("dice5.gif")
            dice.goto(-375, 0)
        if dice_result == 6:
            dice.shape("dice6.gif")
            dice.goto(-375, 0)

        return dice_result - 1

#Function that controls the winning message displayed when a player wins the game
#--------------------------------------------------
def win(player_one_name, player_two_name, remove, player_one_turn, player_one_score, player_two_score, won):
    
    screen = Screen()
    win_draw = Turtle()
    
    win_draw.penup()                               
    screen.addshape(name="win.gif", shape=None)    #Adds the winning image to the bank of shapes

    if remove == True:
        win_draw.hideturtle()   #Clears the winning image and die for the next game to begin
        roll_dice(won)
        
    else:
        win_draw.showturtle()
        win_draw.shape("win.gif")   #Displays the winning image when a player wins the game
        time.sleep(3)

        player_one_score, player_two_score = score(player_one_name, player_two_name, player_one_turn, player_one_score, player_two_score) #Calls the function to update the score for each player

        return player_one_score, player_two_score  #Returns the updated scores so when a new game is started these scores are passed through to the new game
                                                
#Function that updates the scores of each player
#--------------------------------------------------
def score(player_one_name, player_two_name, player_one_turn, player_one_score, player_two_score):

    if player_one_turn == True:
        print("\n" + player_one_name + " wins!")                   
        player_one_score = player_one_score + 1
                   
    else:                                           #Checks if a player has won and updates their score appropriately if they have
        print(player_two_name + " wins!")
        player_two_score = player_two_score + 1

    print("\n***************************")
    print(player_one_name + ": " + str(player_one_score) + " wins")     #Displays each player's current score
    print(player_two_name + ": " + str(player_two_score) + " wins")
    print("***************************")
  
    return player_one_score, player_two_score   #Returns each player's updated score
        
#Function that moves the player on their turn
#--------------------------------------------------
def move_piece(player_one_name, player_two_name, dice_result, player_one, player_two, won, player_one_turn, player_one_score, player_two_score):

    screen = Screen()

    if player_one_turn == True:
        player = player_one
        offset = 30
                                #Checks what players turn to move it is and sets an offset for that game piece's position in each square appropriately,  
    else:                       #so that the square it lands on can be verified correctly
        player = player_two
        offset = -30
    
    old_position = player.pos()    #Saves the player's position before each move
   
    for i in range(0, dice_result + 1):  #Moves the game piece forward the number of squares stated on the die, one square at a time
        current_position = player.pos()  #Saves the player's position after each part of the move 
      
        if str(current_position + (offset, 0)) == str(index_array[4][0]) or str(current_position + (offset, 0)) == str(index_array[4][2]):
            player.goto(current_position + (0, 120))
            player.left(180)
            continue                                                                                  
                                                                                                                                               
        if str(current_position + (offset, 0))  == str(index_array[0][1]) or str(current_position + (offset, 0)) == str(index_array[0][3]):          
            player.goto(current_position + (0, 120))                          
            player.right(180)
            continue

        #Checks whether the player has reached either edge of the board and moves them appropriately
            

        player.forward(120)

        if str(current_position + (120, 0) + (offset, 0)) == str(index_array[4][4]):    #Checks whether the player will make it to the end square with the exact required number of moves
            if i == dice_result:
                
                won = True          #Sets to true if the player wins by reaching the final square in the required number of moves  
                
                remove = False      #Sets the variable remove to false to prevent the gameboard from being reconstructed each game
                
                player_one_score, player_two_score = win(player_one_name, player_two_name, remove, player_one_turn, player_one_score, player_two_score, won)     #Calls the function that deals with a player winning the game

            else:
                player.goto(old_position)   #Returns the player to where they were previously if they have rolled over the number of required moves to make it to the end

            break

    final_position = (player.pos())     #Sets the coordinates of the piece's final position after being moved

    object_check(player, final_position, offset)    #Calls the function to check whether there is a snake or a ladder on that specific square
            
    return won, player_one_score, player_two_score  #Returns whether the player has won the game and each player's score
    
#Function that detects which object a player lands on if any
#--------------------------------------------------
def object_check(player, final_position, offset):

    for x in object_positions.items():
        reference, size = x
        position_column = int(reference[1:2])
        position_row = int(reference[4:5])                            #Checks whether the square a player landed at has a snake or ladder on it
        coordinate = get_coordinate(position_column, position_row)
        
        if str(coordinate) == str(final_position + (offset, 0)):
            object_move(size, final_position, player)              #If so, calls the function to move the player appropriately                                       
                
#Function that moves the player in the event of a snake or ladder
#--------------------------------------------------
def object_move(size, final_position, player):

    if size == 120 or size == -120 or size == -360:
        player.left(180)                               #Changes the direction the player will move across the board in, if required on a different row

    size = (0, size)
    
    player.goto(final_position + size)      #Moves the player by the size of the ladder or snake up or down respectively
    
#Function that runs the gameplay of each game
#--------------------------------------------------
def game(player_one_name, player_two_name, player_one, player_two, player_one_score, player_two_score):

    won = False

    player_one_turn = False   
    
    while won == False:
        if player_one_turn == False:
            player_one_turn = True
            name = player_one_name
                                                      #Switches the player that will move each turn whilst no one has won the game
        else:
            player_one_turn = False
            name = player_two_name

        roll = "x"
        while roll != "":
            print("\n***************************")
            roll = input("\n" + name + " please press enter to roll the die") #Will continuously ask for input to roll the die until enter is pressed
            
        dice_result = roll_dice(won) #Sets the value of the die used to move the player on a turn and displays it 

        print("\nYou rolled a " + str(dice_result + 1)) #Tells the user what value on the die they have rolled
       
        

        #Calls the function to move the player, if the move wins the game the won variable is set to true

        won, player_one_score, player_two_score = move_piece(player_one_name, player_two_name, dice_result, player_one, player_two, won, player_one_turn, player_one_score, player_two_score) 

    return player_one_score, player_two_score #Returns the updated scores for each player so when a new game is started the scores are passed through
            
#Function that allows each player to name themselves
#--------------------------------------------------
def name_players(player_one_name, player_two_name):
    
    while player_one_name == "name_one" or len(player_one_name) < 3  or len(player_one_name) > 12:
        if len(player_one_name) < 3  or len(player_one_name) > 12:
            print("\nA name must be 3 - 12 characters long, please try again")    #Allows player one to enter a chosen name that is within a suitable length

        player_one_name = input("\nPlayer one please enter your desired name:") 

    while player_two_name == "name_two" or len(player_two_name) < 3  or len(player_two_name) > 12 or player_two_name == player_one_name:
        if player_two_name == player_one_name:
            print("\nThe other player has already chosen this name, please choose another")

        if len(player_two_name) < 3  or len(player_two_name) > 12:      #Allows player two to enter a chosen name that is within a suitable length and that is not identical to player one's                                           
            print("\nA name must be 3 - 12 characters long, please try again")
            
        player_two_name = input("\nPlayer two please enter your desired name:") 

    player_one_name = player_one_name.strip()
    player_two_name = player_two_name.strip()
    
    return player_one_name, player_two_name #Returns each player's chosen name
     
#Main function for the program
#--------------------------------------------------
def main(reset, player_one_name, player_two_name, player_one_score, player_two_score):

    player_one_turn = 5
    
    if reset == False:
        draw_board()
        player_one_name, player_two_name = name_players(player_one_name, player_two_name)  #Creates the game board and allows each player to enter their desired name when the game is first started

    reset = True #Assigned to true once the game board is created so that it is not created again when future games commence 

    if reset == True:
        remove = True
        won = True
        win(player_one_name, player_two_name, remove, player_one_turn, player_one_score, player_two_score, won)     #Calls the function to remove the winning image and die after a player has won the game
        
    player_one, player_two = add_pieces()   #Adds the game pieces to their starting positions

    print("\n---------------------------")
    print("New game starting!")
    print("---------------------------")

    player_one_score, player_two_score = game(player_one_name, player_two_name, player_one, player_two, player_one_score, player_two_score)         #Calls the function that begins playing the game

    main(reset, player_one_name, player_two_name, player_one_score, player_two_score)       #Restarts the game after a player wins
    
#-------------------------------------------------
main(reset, player_one_name, player_two_name, player_one_score, player_two_score)
