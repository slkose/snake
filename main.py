from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# set up the screen size, color and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

# import a snake, a food and a scoreboard
snake = Snake()
food = Food()
score = Score()

# have the screen listen for keys and set up keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

# set a flag for while loop
game_on = True

# start the game
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() <= -290 or snake.head.xcor() >= 290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        score.reset()
        snake.reset()

    # detect collision with tail

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()

# set screen to exit on click
screen.exitonclick()
