"""Dictionaries."""

__author__ = "730529937"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert should return a dictionary that inverts keys and values."""
    # Initialize an empty dictionary to store the inverted key-value pairs
    inverted_dict = {}

    # Iterate through the input dictionary
    for key, value in x.items():
        # Check if the value already exists as a key in the inverted dictionary
        if value in inverted_dict:
            # If so, raise a KeyError since encountering more than one of the same key during inversion
            raise KeyError("Duplicate keys found during inversion")
        # Otherwise, add the inverted key-value pair to the inverted dictionary
        inverted_dict[value] = key

    return inverted_dict


def favorite_color(x: dict[str, str]) -> str:
    """Takes a dictionary input of names and favorite colors and returns the color that appears most frequently."""
    # Initialize a dictionary to count the occurrences of each color
    color_count: dict[str, int] = {}

    # Initialize a list to keep track of colors in the order they appear
    color_order = []

    # Iterate through the input dictionary
    for color in x.values():
        # If the color already exists in the count dictionary, increment its count
        if color in color_count:
            color_count[color] += 1
        # Otherwise, initialize its count to 1
        else:
            color_count[color] = 1
            color_order.append(color)

    # Initialize variables to store the most popular color and its count
    most_popular_color = color_order[0]
    max_count = color_count[most_popular_color]

    # Iterate through the list of colors in order of appearance
    for color in color_order:
        # If the count of the current color is greater than the max_count, update most_popular_color and max_count
        if color_count[color] > max_count:
            most_popular_color = color
            max_count = color_count[color]

    return most_popular_color


def count(x: list[str]) -> dict[str, int]:
    """Given a list the function produces a dictionary where each key is a value and each value associated is the count of the number of times the value is in the list."""
    # Initialize an empty dictionary to store the counts of each unique value
    counts: dict[str, int] = {}

    # Loop through each item in the input list
    for item in x:
        # Check if the item is already in the dictionary
        if item in counts:
            # If the item exists, increment its count by 1
            counts[item] += 1
        else:
            # If the item doesn't exist, initialize its count to 1
            counts[item] = 1

    return counts


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Given a list, the function produces a dictionary where each key is an alphabet letter and each value is a list of words that begin with that letter."""
    # Initialize an empty dictionary to store the categorized words
    categorized_words: dict[str, list[str]] = {}

    # Iterate through each word in the input list
    for word in x:
        # Get the first letter of the word in lowercase
        first_letter = word[0].lower()

        # Check if the letter already exists in the dictionary
        if first_letter in categorized_words:
            # If the letter exists, append the word to its corresponding list
            categorized_words[first_letter].append(word)
        else:
            # If the letter doesn't exist, initialize a new list with the word
            categorized_words[first_letter] = [word]

    return categorized_words


def update_attendance(x: dict[str, list[str]], y: str, z: str) -> None:
    """Given a dictionary, this function mutates and returns that dictionary with the updated attendance information."""
    # Check if the day_of_week already exists in the attendance_dict
    if y in x:
        # If it exists, append the student to the list of students for that day
        x[y].append(z)
    else:
        # If it doesn't exist, create a new key-value pair with the day_of_week and a list containing the student
        x[y] = [z]