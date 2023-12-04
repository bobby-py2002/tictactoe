#TICTACTOE GAME
'''function to accept player1 choice of X or O
   if player1 doesnot enter valid input(X/O) 
   keep asking for input till its X/O
   and return the choice
'''
from random import randint
p1=""
p2=""
def player1_choice(p2):
    if p2=="X":
        player1="O"
    elif p2=="O":
        player1="X"  
    else:
        player1=input('Enter X/O for player1: ')
        while(not(player1=="X" or player1=="O")):
            print("Enter valid input\n")
            player1=input('Enter X/O for player1: ')
    return player1

'''function to automatically assign player2 X/O 
    depending on what player1 chooses'''

def player2_choice(p1):
    if p1=="X":
        player2="O"
    elif p1=="O":
        player2="X"
    else:
        player2=input('Enter X/O for player2: ')
        while(not(player2=="X" or player2=="O")):
            print("Enter valid input\n")
        player2=input('Enter X/O for player2: ')
    return player2

def randb_turn():
     x=randint(1,100)
     if x <=50:
        p1=player1_choice(p2="")
        p2=player2_choice(p1)
        #To print the choices of players
        print(f"player1:  {p1}\n",f"\nplayer2:  {p2}\n\n") 
        print("player1 plays first")
        return 1
          
          
     else:
        p2=player2_choice(p1="")
        p1=player1_choice(p2)
        #To print the choices of players
        print(f"player2:  {p2}\n",f"\nplayer1:  {p1}\n\n") 
        print("player2 plays first")
        return 2

randb_turn()
#a labelled tictactoe board
board=[
        ["_"+"  (1)","_"+"  (2)","_"+"  (3)"],
        ["_"+"  (4)","_"+"  (5)","_"+"  (6)"],
        ["_"+"  (7)","_"+"  (8)","_"+"  (9)"]
      ]

#dictionary to map 2d board to single index
dict1={
        "1":(0,0),"2":(0,1),"3":(0,2),
        "4":(1,0),"5":(1,1),"6":(1,2),
        "7":(2,0),"8":(2,1),"9":(2,2)
            }

#list of valid indexes to be taken as input from players
keys=list(dict1.keys())

count=0

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
             bool_exit=True                     #loop variable that will exit the game
    else:
            return False
    return bool_exit

 #the actaul game
def game_start():
    print_board()
    bool_exit=False
    while(
         True
         ):
        turn=randb_turn()
        if turn==1:
            p1_index=str(input("P1- Enter Index(1-9): ")) 
            #ask player1 to place X/O on the given indices
            #this block is used to check if a repeated value has been entered or an invalid value
            #this is to prevent overwriting of p1 and p2
            #for a valid input, from the list of valid indices that valid input is removed
            #when a repeated value of entered by p2/p1 the value is not found in the list and
            #while loop condition is satisfied which asks for a valid value to come out of the loop
            if p1_index not in keys or p1_index not in dict1.keys():
                while(p1_index not in keys or p1_index not in dict1.keys()):
                    p1_index=str(input("P1- Enter Index(1-9): "))    
        
            board[dict1[p1_index][0]][dict1[p1_index][1]]=p1
            #assign the X/O to the index entered by player
            
            keys[keys.index(p1_index)]="done"
            #remove the index entered from the list of indices to prevent repition

            print_board()
            #print the board to see the outcome

            bool_exit=winner()
            #TIE checking
            if(keys.count("done")==9):
                print("\t!!!TIE!!!")
                break
            #outcome is decided from winner function which shall turn the exit variable true
            #this way game is exited when there is a winner

            if bool_exit==True:
                print("\t!!!Player1 Wins!!!")
                break
        #similar code for player 2
            p2_index=str(input("P2- Enter Index(1-9): "))
            if p2_index not in keys or p2_index not in dict1.keys():
                while(p2_index not in keys or p2_index not in dict1.keys()):
                    p2_index=str(input("P2- Enter Index(1-9): "))

            keys[keys.index(p2_index)]="done"
            
            board[dict1[p2_index][0]][dict1[p2_index][1]]=p2
            
            print_board()
            bool_exit=winner()
            #TIE checking
            if(keys.count("done")==9):
                print("!!!TIE!!!")
                break
            
            
            if bool_exit==True:
                print("\t!!!Player2 Wins!!!")
                break  
        else:
        #similar code for player 2
            p2_index=str(input("P2- Enter Index(1-9): "))
            if p2_index not in keys or p2_index not in dict1.keys():
                while(p2_index not in keys or p2_index not in dict1.keys()):
                    p2_index=str(input("P2- Enter Index(1-9): "))

            keys[keys.index(p2_index)]="done"
            
            board[dict1[p2_index][0]][dict1[p2_index][1]]=p2
            
            print_board()
            bool_exit=winner()
            #TIE checking
            if(keys.count("done")==9):
                print("!!!TIE!!!")
                break
            
            
            if bool_exit==True:
                print("\t!!!Player2 Wins!!!")
                break  

            p1_index=str(input("P1- Enter Index(1-9): ")) 
            #ask player1 to place X/O on the given indices
            #this block is used to check if a repeated value has been entered or an invalid value
            #this is to prevent overwriting of p1 and p2
            #for a valid input, from the list of valid indices that valid input is removed
            #when a repeated value of entered by p2/p1 the value is not found in the list and
            #while loop condition is satisfied which asks for a valid value to come out of the loop
            if p1_index not in keys or p1_index not in dict1.keys():
                while(p1_index not in keys or p1_index not in dict1.keys()):
                    p1_index=str(input("P1- Enter Index(1-9): "))    
        
            board[dict1[p1_index][0]][dict1[p1_index][1]]=p1
            #assign the X/O to the index entered by player
            
            keys[keys.index(p1_index)]="done"
            #remove the index entered from the list of indices to prevent repition

            print_board()
            #print the board to see the outcome

            bool_exit=winner()
            #TIE checking
            if(keys.count("done")==9):
                print("\t!!!TIE!!!")
                break
            #outcome is decided from winner function which shall turn the exit variable true
            #this way game is exited when there is a winner

            if bool_exit==True:
                print("\t!!!Player1 Wins!!!")
                break
game_start()
