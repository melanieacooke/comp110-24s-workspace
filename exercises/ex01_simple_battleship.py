"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730529937"

user1_input: str = input("Pick a secret boat location between 1 and 4: ")
input_number: int = int(user1_input)
blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"
emoji_boxes: str = ""


if input_number <= 0:
    print("Error! " + user1_input + " is too low!")
    
if input_number >= 5:
    print("Error! " + user1_input + " is too high!")


guess_input: str = input("Guess a number between 1 and 4: ")
guess_number: int = int(guess_input)
result: str = red_box if input_number == guess_number else white_box

if guess_number <= 0:
    print("Error! " + guess_input + " too low!")

if guess_number >= 5:
    print("Error! " + guess_input + " too high!")

if guess_number != int:
    exit()

if guess_number == 1:
    emoji_boxes += result
else:
    emoji_boxes += blue_box

if guess_number == 2:
    emoji_boxes += result
else:
    emoji_boxes += blue_box

if guess_number == 3:
    emoji_boxes += result
else:
    emoji_boxes += blue_box

if guess_number == 4:
    emoji_boxes += result
else:
    emoji_boxes += blue_box

print(emoji_boxes)

if guess_number == input_number:
    print("Correct! You hit the boat.")
else:
    print("Incorrect! You missed the boat.")












