import turtle


collist = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
collist2 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
collist3 = ['thistle', 'rosybrown', 'peachpuff', 'khaki', 'darkkhaki', 'olive']
listsel = collist3
angle = 125   # 125
linewidth = 2
fadespeed = 30


def start():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(10, 1)    # use this to control animation speed
    turtle.penup()
    turtle.right(-135)
    turtle.forward(330)
    turtle.right(135)
    turtle.pensize(linewidth)
    turtle.pendown()


def loop():
    c = 0
    for i in range(1000):
        c = forward_loop(c)
        turtle.right(angle)
        currentposx, currentposy = round(turtle.xcor()), round(turtle.ycor())
        if currentposx == startx and currentposy == starty:
            turtle.hideturtle()
            turtle.penup()
            print('breaking')
            turtle.exitonclick()
    return c


def forward_loop(countn):
    for i in range(500//fadespeed):
        if countn > len(listsel) - 1:
            countn = 0
        turtle.color(listsel[countn])
        turtle.forward(fadespeed)
        countn += 1
    return countn


# def forward_loop2(countn):
#     sc = 0
#     for i in range(500//fadespeed):
#         if countn > len(listsel) - 1:
#             countn = 0
#         turtle.color(listsel[countn])
#         turtle.forward(fadespeed)
#         countn += 1
#     return countn


start()
startx, starty = round(turtle.xcor()), round(turtle.ycor())

print(startx, starty)
loop()
