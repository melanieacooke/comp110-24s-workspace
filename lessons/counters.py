"""Practicing Counters"""
#keeping track of the count of stuff

num_string: str = "123"
length: int = int(num_string)
#how many odd numbers are in num_string
num_of_odds: int = 0
 
if int(num_string[0]) % 2 == 1:
    num_of_odds = num_of_odds + 1

if int(num_string[1]) % 2 == 1:
    num_of_odds = num_of_odds + 1

if int(num_string[2]) % 2 == 1:
    num_of_odds = num_of_odds + 1

print(num_of_odds)

