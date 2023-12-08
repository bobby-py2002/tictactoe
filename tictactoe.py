#TICTACTOE GAME
'''function to accept player1 choice of X or O
   if player1 doesnot enter valid input(X/O) 
   keep asking for input till its X/O
   and return the choice
'''
from random import randint

#global variables
global p1
global p2
global turn
global bool_exit
p1 = ""
p2 = ""


#board initialization function
def initialize_board():
        tttboard= [
            ["_"+"  (1)","_"+"  (2)","_"+"  (3)"],
            ["_"+"  (4)","_"+"  (5)","_"+"  (6)"],
            ["_"+"  (7)","_"+"  (8)","_"+"  (9)"]
        ]
        return tttboard

#2 players choose using single choice function
def player_choice(player, other_player):
    global p1, p2  # Declare p1 and p2 as global variables
    choice = ""
    
    while choice not in ["X", "O"]:
        choice = input(f"Enter X/O for {player}: ")
        
        if choice not in ["X", "O"]:
            print("Enter valid input\n")
    
    if player == "player1":
        p1 = choice
        p2 = "O" if p1 == "X" else "X"
        print(f"{player}: {p1}\n{other_player}: {p2}\n\n")
    elif player == "player2":
        p2 = choice
        p1 = "O" if p2 == "X" else "X"
        print(f"{player}: {p2}\n{other_player}: {p1}\n\n")
    
    return choice

# function to randomly assign 1st turn to either player
def randb_turn():
     global turn
     x = randint(1, 10)
     
     if x <= 5:
        player_choice("player1", "player2")
        print("player1 plays first")
        turn = 1
     else:
        player_choice("player2", "player1")
        print("player2 plays first")
        turn = 2

global board
board=initialize_board()

# function to print the board in 2d manner
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],"\t\t",end="")
        print("\n\n")

#function to stop the game when 1 out of 8 ways to win tictactoe is fullfilled
def winner():
    if(
            board[0][0]==board[0][1]==board[0][2]
            or
            board[1][0]==board[1][1]==board[1][2]
            or 
            board[2][0]==board[2][1]==board[2][2]
            or
            board[0][0]==board[1][0]==board[2][0]
            or 
            board[0][1]==board[1][1]==board[2][1]
            or
            board[0][2]==board[1][2]==board[2][2]
            or
            board[0][0]==board[1][1]==board[2][2]
            or
            board[0][2]==board[1][1]==board[2][0]
           ):
            return True                     #loop variable that will exit the game
    else:
            return False
    
#function to be executed if player wants to play again
def play_again(again):
    global bool_exit
    global board
    bool_exit=False
    print("PLAY AGAIN?\n")
    again=input("y/n\n")
    if again not in ["y","n"]:
            while(again not in ["y","n"]):
                again=input("y/n\n")
    if again=="y":
                board=initialize_board()
                game_start()

def index_check(index,keys,dict1,pturn):
        if pturn==0:
            if index not in keys or index not in dict1.keys():
                while(index not in keys or index not in dict1.keys()):
                    index=str(input("P1- Enter Index(1-9): "))
        else:
            if index not in keys or index not in dict1.keys():
                while(index not in keys or index not in dict1.keys()):
                    index=str(input("P1- Enter Index(1-9): "))
        return index    

     
                
#the actaul game
def game_start():
    #dictionary to map 2d board to single index
    dict1={
            "1":(0,0),"2":(0,1),"3":(0,2),
            "4":(1,0),"5":(1,1),"6":(1,2),
            "7":(2,0),"8":(2,1),"9":(2,2)
                }

    #list of valid indexes to be taken as input from players
    keys=list(dict1.keys())

    #decide turn
    randb_turn()

    #variable to keep track if player wants to play again
    again=""

    print_board()

    bool_exit=False
    while(
         True
         ):
            if(turn==1):
                
                p1_index=str(input("P1- Enter Index(1-9): "))
                '''ask player1 to place X/O on the given indices
                   this block is used to check if a repeated value has been entered or an invalid value
                   this is to prevent overwriting of p1 and p2
                   for a valid input, from the list of valid indices that valid input is removed
                   when a repeated value of entered by p2/p1 the value is not found in the list and
                   while loop condition is satisfied which asks for a valid value to come out of the loop'''
                
                pturn=0
                p1_index=index_check(p1_index,keys,dict1,pturn) 
            
                board[dict1[p1_index][0]][dict1[p1_index][1]]=p1
                #assign the X/O to the index entered by player
                
                keys[keys.index(p1_index)]="done"
                #remove the index entered from the list of indices to prevent repition

                print_board()
                #print the board to see the outcome

                #check winner
                bool_exit=winner()
                if bool_exit==True:
                    print("\t!!!Player1 Wins!!!")
                    play_again(again)
                    break
                    
                #TIE checking
                if(keys.count("done")==9):
                    print("\t!!!TIE!!!")
                    play_again(again)
                    break

                #outcome is decided from winner function which shall turn the exit variable true
                #this way game is exited when there is a winner

                p2_index=str(input("P2- Enter Index(1-9): "))
                pturn=1
                p2_index=index_check(p2_index,keys,dict1,pturn)

                keys[keys.index(p2_index)]="done"
                
                board[dict1[p2_index][0]][dict1[p2_index][1]]=p2
                
                print_board()
                bool_exit=winner()
                
                if bool_exit==True:
                    print("\t!!!Player2 Wins!!!")
                    play_again(again)
                    break
                if(keys.count("done")==9):
                    print("!!!TIE!!!")
                    play_again(again)
                    break
                    
            else:
                p2_index=str(input("P2- Enter Index(1-9): "))
                pturn=1
                p2_index=index_check(p2_index,keys,dict1,pturn)

                keys[keys.index(p2_index)]="done"
                
                board[dict1[p2_index][0]][dict1[p2_index][1]]=p2

                print_board()

                bool_exit=winner()
            
                if bool_exit==True:
                    print("\t!!!Player2 Wins!!!")
                    play_again(again)
                    break  
                if(keys.count("done")==9):
                    print("\t!!!TIE!!!")
                    play_again(again)
                    break
                    
                
                p1_index=str(input("P1- Enter Index(1-9): "))
                pturn=0 
                p1_index=index_check(p1_index,keys,dict1,pturn)    
            
                board[dict1[p1_index][0]][dict1[p1_index][1]]=p1
                keys[keys.index(p1_index)]="done"
            
                print_board()
            
                bool_exit=winner()
                
                if bool_exit==True:
                    print("\t!!!Player1 Wins!!!")
                    play_again(again)
                    break
                if(keys.count("done")==9):
                    print("\t!!!TIE!!!")
                    play_again(again)
                    break
game_start()
