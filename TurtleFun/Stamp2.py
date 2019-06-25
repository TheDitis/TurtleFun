from turtle import *


collist1 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
colsel = collist1

wn = Screen()
jose = Turtle()
jose.shape("circle")
jose.penup()
jose.resizemode("auto")
jose.speed(10)


def stamp_circle(s):
    jose.pensize(s * 2)
    jose.color(colsel[s])
    for size in range(10):
        jose.forward(s * 50)
        jose.stamp()
        jose.forward(s * -50)
        jose.right(36)


for i in range(20):
    stamp_circle(i)

jose.hideturtle()

wn.exitonclick()





