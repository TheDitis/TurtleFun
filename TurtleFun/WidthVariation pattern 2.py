import turtle

bestsettings = [[500, 90.2, 0.9]]
collist = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
bigcollist = collist * 500
widthrange = [1, 10]
linewidth = 2
RoC = 600
angle1 = 130
shiftamt = 0.9

setting = 0
# RoC = bestsettings[setting][0]
# angle1 = bestsettings[setting][1]
# shiftamt = bestsettings[setting][2]


widthlist = list(range(widthrange[0], widthrange[1])) + list(range(widthrange[1],widthrange[0] - 1, -1))


def start():
    turtle.bgcolor("black")
    turtle.speed(5000)
    turtle.penup()
    # turtle.right(-135)
    # turtle.forward(330)
    # turtle.right(133.5)
    turtle.goto(-RoC/2, RoC/2)
    turtle.pendown()
    turtle.color(bigcollist[0])


def loop():
    count = 0
    for c in bigcollist:
        for i in widthlist:
            turtle.pensize(i)
            turtle.forward(RoC)
            count += 1
            turtle.right(angle1)
            if count > 20:
                globals()['RoC'] = inward()
                count = 0
                turtle.color(c)



def inward():
    turtle.penup()
    turtle.setpos(turtle.xcor() * shiftamt, turtle.ycor() * shiftamt)
    globals()['widthlist'] = [i * shiftamt for i in widthlist]
    # globals()['widthlist'] = [i == 0 for i in widthlist if i < 1]
    turtle.pendown()
    return round(RoC * shiftamt)


print(widthlist)
start()
loop()
