import os

board = [" "," "," "," "," "," "," "," "," "]
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'

def DrawBoard():
  print(" %c | %c |%c " % (board[0],board[1],board[2]))
  print("___|___|___")
  print(" %c | %c |%c " % (board[3],board[4],board[5]))
  print("___|___|___")  
  print(" %c | %c |%c " % (board[6],board[7],board[8]))
  print("   |   |   ")

  # hello

def CheckPosition(x):
  if(board[x] == ' '):
    return True
  else:
    return False

def CheckWin():
  global Game

  if(board[0] == board[1] and board[1] == board[2] and board[0] != ' '):
    Game = Win
  elif(board[3] == board[4] and board[4] == board[5] and board[3] != ' '):
    Game = Win
  elif(board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
    Game = Win

  elif(board[0] == board[3] and board[3] == board[6] and board[3] != ' '):
    Game = Win
  elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
    Game = Win
  elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
    Game = Win

  elif(board[0] == board[4] and board[4] == board[8] and board[0] != ' '):
    Game = Win
  elif(board[2] == board[4] and board[4] == board[6] and board[2] != ' '):
    Game = Win

  elif(board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
    Game = Draw
  
  else:
    Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]")
print()
print("Please wait...")
while(Game == Running):
  os.system("cls")
  DrawBoard()
  if(player % 2 != 0):
    print("Player 1's chance")
    Mark = 'X'
  else:
    print("Player 2's chance")
    Mark = 'O'
  choice = int(input("Enter position between 0-8 where you want to mark:"))
  if(CheckPosition(choice)):
    board[choice] = Mark
    player += 1
    CheckWin()

os.system("cls")
DrawBoard()
if(Game == Draw):
  print("Game Draw")
elif(Game == Win):
  player -= 1
  if(player % 2 != 0):
    print("Player 1 won")
  else:
    print("Player 2 won")