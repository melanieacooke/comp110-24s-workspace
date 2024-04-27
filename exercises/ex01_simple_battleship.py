"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730529937"

user1_input: str = input("Pick a secret boat location between 1 and 4: ")
input_number: int = int(user1_input)
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
emoji_boxes: str = ""


if input_number <= 0:
    print("Error! " + user1_input + " too low!")
    exit()
    
if input_number >= 5:
    print("Error! " + user1_input + " too high!")
    exit()

user2_input: str = input("Guess a number between 1 and 4: ")
input_guess: int = int(user2_input)

if input_guess <= 0:
    print("Error! " + user2_input + " too low!")
    exit()
    
if input_guess >= 5:
    print("Error! " + user2_input + " too high!")
    exit()

if input_guess == input_number:
    result += RED_BOX
else:
    result += WHITE_BOX

if input_guess == 1:
    emoji_boxes += result
else:
    emoji_boxes += BLUE_BOX

if input_guess == 2:
    emoji_boxes += result
else:
    emoji_boxes += BLUE_BOX

if input_guess == 3:
    emoji_boxes += result
else:
    emoji_boxes += BLUE_BOX

if input_guess == 4:
    emoji_boxes += result
else:
    emoji_boxes += BLUE_BOX

print(emoji_boxes)

if input_guess == input_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")