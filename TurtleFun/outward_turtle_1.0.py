import turtle

angle = 5
collist2 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
linewidth = 1
rate = 0.01
instant = 1


def setup_turtle():
    turtle.bgcolor('black')
    turtle.tracer(10, 1)
    if instant:
        turtle.tracer(0, 0)
    turtle.pensize(linewidth)
    turtle.pendown()


def loop():
    for i in range(10000):
        colsel = i % len(collist2)
        turtle.color(collist2[colsel])
        fwdamt = rate * i
        turtle.forward(fwdamt)
        # forward_color_split(fwdamt)
        turtle.left(angle)
    turtle.exitonclick()


def forward_color_split(totlen):
    for i in range(len(collist2)):
        divamt = totlen / len(collist2)
        turtle.color(collist2[i])
        turtle.forward(divamt)


setup_turtle()
loop()