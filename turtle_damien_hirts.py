from turtle import Turtle, Screen
import turtle as t
import random
import colorgram


def print_dot():
    col = random.choice(colors)
    tim.dot(30, (col.rgb.r, col.rgb.g, col.rgb.b))


colors = colorgram.extract('image.png', 20)


screen = Screen()
tim = Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setposition(-300, -300)
h = 0
while h < 500:
    w=0
    while w < 500:
        w += 50
        tim.goto(w-300,h-300)
        print_dot()
    h += 50

#tim.hideturtle()




screen.exitonclick()


