from turtle import *


collist1 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
colsel = collist1
print(len(collist1))

wn = Screen()
wn.bgcolor('black')
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
    for j in range(10000):
        count = (j + 1) % (len(colsel) - 1)
        jose.pensize((j * 2) / 40)
        jose.color(colsel[count])
        jose.forward((j ** 2) / 500)
        jose.stamp()
        jose.backward((j ** 2) / 500)
        jose.right(360 / circlenum)


for i in range(50):
    stamp_circle(i)

jose.hideturtle()

wn.exitonclick()





