from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
LIMIT_WALL = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title("My snake game")
screen.tracer(0)
screen.listen()


boarder = Turtle()
boarder.color("White")
boarder.penup()
boarder.goto(-300, 300)
boarder.pendown()
for _ in range(4):
    boarder.fd(600)
    boarder.right(90)

food = Food()
snake = Snake()
scoreboard = Scoreboard()


game_is_on = True

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.eating()
        scoreboard.refresh_score()
    # detect collision with wall
    if (snake.head.xcor() > LIMIT_WALL or snake.head.xcor() < -LIMIT_WALL or snake.head.ycor() > LIMIT_WALL
            or snake.head.ycor() < -LIMIT_WALL):
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
    if snake.check_body_collision():
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
