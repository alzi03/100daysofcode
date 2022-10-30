from snakesetup import Snaking
from level import Dot
from turtle import Screen
import time


def snakegame():
    dot = Dot()
    dot.go()

    snake = Snaking()  # using the new class made
    screen = Screen()  # setups the screen

    snake.window(screen)

    screen.onkey(snake.up, 'Up')  # arrow keys to move snake
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.right, 'Right')

    apples = 0

    safe = True
    while safe: # constantly moving
        snake.scoretracker(apples)  # add a score tracker
        screen.update()  # added so all turtles move at once rather than with delay
        time.sleep(0.1)
        snake.forward()
        if snake.front.distance(dot) <= 20:  # point system
            dot.disappear()
            snake.addpoint()
            apples += 1
        if snake.death():  # touches border or touches tail
            break

















snakegame()
