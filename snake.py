from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
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
        for position in COORDINATES:
            self.add_part(position)

    def add_part(self, position):
        part = Turtle(shape="square")
        part.penup()
        part.color("white")
        part.goto(position)
        self.snake.append(part)

    def extend(self):
        self.add_part(self.snake[-1].position())

    def reset(self):
        for part in self.snake:
            part.setposition(x=1000, y=1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move_snake(self):
        snake_len = len(self.snake)
        for x in range(snake_len - 1):
            self.snake[(snake_len - x - 1)].goto(self.snake[(snake_len - x - 2)].position())
        self.snake[0].forward(MOVING_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
