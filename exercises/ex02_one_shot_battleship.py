"""One Shot Battleship."""

__author__ = "730529937"

grid_size = 4
secret_row = 3
secret_column = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

user_input = input("Guess a row: ")
guess_row = int(user_input)
# Prompt the user to guess a row
while guess_row > 4 or guess_row < 0:
    user_input = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    guess_row = int(user_input)

    
user_input2 = input("Guess a column: ")
guess_column = int(user_input2)
# Prompt the user to guess a column
while guess_column > 4 or guess_column < 0:
    user_input2 = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    guess_column = int(user_input2)


row_counter = 1
result_box = WHITE_BOX

# Loop through rows
while row_counter <= grid_size:
    # Initialize emoji string for a singular row
    emoji_row = ""
    
    # Initialize column counter variable
    column_counter = 1
    
    # Test if the user's row guess is equal to the row counter
    if guess_row == row_counter:
        # Loop through columns
        while column_counter <= grid_size:
            # Check if user's column guess is equal to the counter
            if guess_column == column_counter:
                if guess_row == secret_row and guess_column == secret_column:
                    result_box = RED_BOX
                else:
                    result_box = WHITE_BOX
                emoji_row += result_box
            else:
                emoji_row += BLUE_BOX
            # Increment column counter
            column_counter += 1
    else:
        # Loop through columns
        while column_counter <= grid_size:
            emoji_row += BLUE_BOX
            # Increment column counter
            column_counter += 1
    
    # Print the emoji string for one row
    print(emoji_row)
    
    # Increment row counter
    row_counter += 1

# Check if the guess matches the secret location
if guess_row == 3 and guess_column == 2:
    print("Hit!")
elif guess_row == 3 and guess_column != 2:
    print("Close! Correct row, wrong column.")
elif guess_column == 2 and guess_row != 3:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
    