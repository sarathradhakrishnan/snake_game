from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
x = 0
y = 10

for number in range(0, 3):
    new = Turtle("square")
    new.color("white")
    new.goto(x, y)
    x = x - 20

screen.exitonclick()
