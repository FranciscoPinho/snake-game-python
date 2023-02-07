from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for number in range(3):
            snake_square = Turtle(shape="square")
            snake_square.color("white")
            snake_square.penup()
            snake_square.setx(-20 * number)
            self.snake.append(snake_square)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for segment_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_num - 1].xcor()
            new_y = self.snake[segment_num - 1].ycor()
            self.snake[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        snake_square = Turtle(shape="square")
        snake_square.color("white")
        snake_square.penup()
        snake_square.goto(self.snake[-1].position())
        self.snake.append(snake_square)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
