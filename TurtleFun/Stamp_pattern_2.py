from turtle import *


collist1 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
colsel = collist1
print(len(collist1))

wn = Screen()
jose = Turtle()
jose.shape("circle")
jose.penup()
jose.resizemode("auto")
jose.speed(10)
circlenum = 46
tracer(8, 1)
jose.hideturtle()

count = 0


def stamp_circle(s):
    jose.pensize(s * 2)
    for j in range(circlenum):
        jose.color(colsel[count])
        jose.forward(s**2)
        jose.stamp()
        jose.forward(-(s**2))
        jose.right(360 / circlenum)
        globals()['count'] += 1
        if count > len(colsel) - 1:
            globals()['count'] = 0


for i in range(50):
    stamp_circle(i)

jose.hideturtle()

wn.exitonclick()





