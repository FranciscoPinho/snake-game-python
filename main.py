from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.set_high_score_from_file()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            break

screen.exitonclick()