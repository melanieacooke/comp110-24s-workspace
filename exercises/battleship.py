"""One Shot Battleship."""

__author__ = "730529937"


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Size of the grid
grid_size = 4

# Secret location
secret_row = 3
secret_column = 2

# Get user guesses
guess_row = int(input("Guess a row: "))
guess_column = int(input("Guess a column: "))

# Check if user guesses are within grid boundaries
while guess_row > grid_size or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")
    guess_row = int(input("Guess a row: "))
    guess_column = int(input("Guess a column: "))

# Initialize row counter variable
row_counter = 1

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
                # If the guess matches the secret location, print a red box
                if guess_row == secret_row and guess_column == secret_column:
                    emoji_row += RED_BOX
                    print("Hit!")
                else:
                    # If only the row or column is correct, print a hint
                    if guess_row == secret_row:
                        print("Close! Correct column, wrong row.")
                    elif guess_column == secret_column:
                        print("Close! Correct row, wrong column.")
                    else:
                        # If both row and column are wrong, print a miss
                        print("Miss!")
                    emoji_row += WHITE_BOX
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


"""One Shot Battleship."""

__author__ = "730529937"

grid_size = 4
secret_row = 3
secret_column = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Prompt the user to guess a row
while True:
    user_input = input("Guess a row: ")
    guess_row = int(user_input)
    if guess_row <= 3 or guess_row >= 0:
        if 1 <= guess_row <= grid_size:
         break  
        else:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        print("Invalid input. Please enter a valid number.")

# Prompt the user to guess a column
while True:
    user_input = input("Guess a column: ")
    guess_column = int(user_input)
    if guess_column <= 2 or guess_column >= 0:
        if 1 <= guess_column <= grid_size:
            break
        else:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else:
        print("Invalid input. Please enter a valid number.")


row_counter = 1

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
                emoji_row += RED_BOX
            else:
                emoji_row += WHITE_BOX
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
else:
    print("Miss!")
