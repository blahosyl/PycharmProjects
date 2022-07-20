from turtle import Turtle, Screen
import random
#aliasing: if you want to shorten the module name
#import turtle as t

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange")

screen =Screen()
#alternatively: #`import turtle` at the beginning, then `turtle.colormode(255)`


# #draw a square
# for _ in range(4): # do this 4 times
#     timmy.forward(100)
#     timmy.right(90)

# #draw a dashed line
# for _ in range(15): # do this 15 times
#     timmy.forward(10)
#     timmy.penup() #stop drawing when moving
#     timmy.forward(10) #start drawing when moving
#     timmy.pendown()

# #draw shapes from triangle to decagon
# sides = 3
# while sides < 11:
#     # random color
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     timmy.pencolor(r, g, b)
#
#     angle = 360/sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#     sides += 1


#change shape of turtle
#timmy.shape("circle")

#random walk with random color
# for _ in range (10):
#     timmy.width(width=8)
#     # random color
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     timmy.pencolor(r, g, b)
#
#     # random walk
#     direction = random.choice([90, 180, -90, 0])
#     timmy.forward(20)
#     timmy.right(direction)

def random_color():
    """Returns a random RGB color"""
    import turtle
    turtle.colormode(255)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcolor = (r, g, b)
    return randcolor

def spirograph(circles):
    # increase speed
    timmy.speed("fastest")
    timmy.shape("circle")
    timmy.shapesize(0.5)
    angle = 360/circles #multiply by -1 to start drawing in the other direction

    for _ in range (circles):
        timmy.pencolor(random_color())
        timmy.circle(60, extent=None, steps=None)
        timmy.right(angle)

spirograph(100)



#this has to come at the bottom of the file
screen.exitonclick()
