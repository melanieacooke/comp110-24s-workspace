"""Various Fun Turtle Functions."""

__author__ = "730529937" 

from turtle import Turtle, colormode, done


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width starting from the bottom left corner at (x, y)."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0)  # Face the turtle to the right
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(width)
        a_turtle.left(90)


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle starting from the bottom left corner at (x, y)."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0)  # Face the turtle to the right
    a_turtle.pendown()
    for i in range(2):
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)


def draw_house(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Draws the house at a starting point (x, y), which is the bottom left corner."""
    draw_square(a_turtle, x, y, size)  # Main house structure


def draw_window(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Draws a window at the specified location with a given size."""
    a_turtle.pencolor('blue')  # Change the pen color
    draw_square(a_turtle, x, y, size)  # Using the square function


def draw_door(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws a door at the specified location."""
    a_turtle.fillcolor('brown')  # Set fill color to brown
    draw_rectangle(a_turtle, x, y, width, height)  # Use rectangle function for the door


def main() -> None:
    """Main function to set up the turtle environment and draw the scene."""
    colormode(255)  # Allows us to use RGB color values
    house_turtle = Turtle()
    house_turtle.speed('fastest')

    # Draw the house
    draw_house(house_turtle, -100, -100, 200)  # Start at -100, -100 to center the house

    # Draw windows, positioned relative to the house's position
    draw_window(house_turtle, -75, 20, 30)  # Left window
    draw_window(house_turtle, 45, 20, 30)   # Right window

    # Draw door, centered at the bottom of the house
    draw_door(house_turtle, -20, -100, 40, 60)  # Door position to be bottom center

    done()


if __name__ == "__main__":
    main()
