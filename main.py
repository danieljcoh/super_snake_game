import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from super_food import SuperFood
from scoreboard import Scoreboard
import time


# Functions
def turn_right():
    Turtle.right(90)


# Screen Setup
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Super Snake")

# Creating Turtles
snake = Snake()
food = Food()
scoreboard = Scoreboard()
super_food = SuperFood()

# Player Controller Movement
screen.onkey(key="Up", fun=snake.snake_up)
screen.onkey(key="Down", fun=snake.snake_down)
screen.onkey(key="Right", fun=snake.snake_right)
screen.onkey(key="Left", fun=snake.snake_left)

# Turtle Setup
game_is_on = True

# time
game_time = .2

while game_is_on:

    if scoreboard.score >= 25:
        super_food.shapesize(stretch_len=.1, stretch_wid=.1)
        game_time = .02
    elif scoreboard.score >= 20:
        game_time = .04
    elif scoreboard.score >= 15:
        game_time = .05
        super_food.shapesize(stretch_len=.4, stretch_wid=.4)
    elif scoreboard.score >= 10:
        game_time = .1
        super_food.shapesize(stretch_len=.5, stretch_wid=.5)
    elif scoreboard.score >= 5:
        game_time = .15
        super_food.shapesize(stretch_len=.7, stretch_wid=.7)

    screen.update()
    time.sleep(game_time)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.clear()
        scoreboard.increase_score()

    # Collision with super_food
    if snake.head.distance(super_food) < 15:
        super_food.refresh()
        scoreboard.clear()
        scoreboard.increase_score_super_food()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


