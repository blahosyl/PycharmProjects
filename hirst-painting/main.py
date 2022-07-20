import colorgram

import random

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)

# get the colors from the image, up to the number specified in the second argument
# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# then check the colors with https://www.w3schools.com/colors/colors_rgb.asp to see which ones are just different shades
# of white. The closer all 3 numbers are to 255, the more likely the color is just a sort of "almost-white" shade.
# Resulting list below:

rgb_colors = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46),
              (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97),
              (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23),
              (21, 188, 230),  (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182),
              (180, 187, 211)]


# draw random color dots, 10x10 grid, dot size 20, space between dots 50

def dot_row(x: int):
    """Draws a row of x dots, dot size 20, space between dots 50"""
    for _ in range(x):  # do this x times
        turtle.hideturtle()
        turtle.penup()
        turtle.color(random.choice(rgb_colors))
        turtle.dot(20)
        turtle.forward(50)


def dot_matrix(x: int, y: int):
    """Draws a matrix of dots consisting of x columns and y rows, dot size 20, space between dots 50
    (calls the function `dot_row(x)`"""
    turtle.hideturtle()
    turtle.penup()
    # move the turtle to the correct position so the dot matrix will be more or less centered
    start_x = (-x/2)*50
    start_y = -y/2
    turtle.setpos(start_x, start_y)

    for _ in range(y):
        turtle.penup()
        turtle.setpos(start_x, (_+start_y)*50)
        dot_row(x)
    # if you want the turtle to go back to "normal mode, uncomment the lines below"
    # turtle.pendown()
    # turtle.showturtle()


turtle.speed("fastest")

dot_matrix(10, 10)

# this has to come at the bottom of the file
screen.exitonclick()
