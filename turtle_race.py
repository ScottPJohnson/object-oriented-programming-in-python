from turtle import Turtle
from random import randint

scott = Turtle()
scott.color('red')
scott.shape('turtle')
scott.penup()
scott.goto(-160, 100)
scott.pendown()

kate = Turtle()
kate.color('yellow')
kate.shape('turtle')
kate.penup()
kate.goto(-160, 70)
kate.pendown()

jack = Turtle()
jack.color('blue')
jack.shape('turtle')
jack.penup()
jack.goto(-160, 40)
jack.pendown()

harris = Turtle()
harris.color('green')
harris.shape('turtle')
harris.penup()
harris.goto(-160, 10)
harris.pendown()

for movement in range(100):
    scott.forward(randint(1,5))
    kate.forward(randint(1,5))
    jack.forward(randint(1,5))
    harris.forward(randint(1,5))