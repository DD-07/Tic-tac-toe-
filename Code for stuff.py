# Function - to alternate between two players
def swapping():
  canvas = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
  x_true = True
  game_over = False
  while not game_over: 
    show_game(canvas)
    try:
      choice = convert_into_grid(ask_for_grid())
      place_x(choice, x_true, canvas)
    except ValueError:
      print("Please input a number between and including 1 to 9 that is empty.")
      continue
    game_over = is_win(canvas) or is_over(canvas)
    x_true = not x_true

# Function - to check if all the boxes are full
def is_over(canvas):
  for row in canvas:
    for cont in row:
      if cont == "_":
        return False
  show_game(canvas)
  print("There are no more empty spots, this is a draw!")
  return True

#Function - to check for a winner
def is_win(canvas):
  winner = None # Null value in Python
  # Horizontal check
  for i in range(3):
    if canvas[i][0] == canvas[i][1] == canvas[i][2] and canvas[i][0] != "_":
      winner = canvas[i][0]
      break
    # Vertical check
    if canvas[0][i] == canvas[1][i] == canvas[2][i] and canvas[0][i] != "_":
      winner = canvas[0][i]
      break
  # Diagonal check
  if canvas[1][1] != "_":
    if (canvas[0][0] == canvas[1][1] == canvas[2][2] or canvas[0][2] == canvas[1][1] == canvas[2][0]):
      winner = canvas[1][1]
  if winner is not None:
    show_game(canvas)
    print(f"{winner} is the winner!")
    return True
  return False
     

#Function - to convert the grid chosen to insert into the board
def convert_into_grid(choice):
  choice -= 1
  return(choice // 3, choice % 3)

#Function - to put the data into the board itself
def place_x(choice, x_true, canvas):
    i, j = choice
    if canvas[i][j] == "_":
      canvas[i][j] = "X" if x_true else "O"
    else:
      raise ValueError

#Function - To display the canvas in a better way
def show_game(canvas):
  for row in canvas:
    print(row)
  
#Function - to ask for which grid the user wants  
def ask_for_grid():
  choice = int(input("What grid do you choose?"))
  if not 1 <= choice <= 9:
    raise ValueError
  return choice


#start of the game

print("Welcome to tic tac toe, the classic original game! This is just like the original, just coded using python. Two players will be needed.")

print(" The grids will be numbered from 1 to 9, from left to right, from top to bottom.")

# List - for the tic tac toe board
canvas = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

swapping()

