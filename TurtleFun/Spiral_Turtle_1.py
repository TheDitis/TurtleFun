import turtle

collist1 = ['red', 'crimson', 'orangered', 'darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'limegreen', 'springgreen', 'mediumspringgreen', 'aquamarine', 'turquoise', 'aqua', 'deepskyblue', 'dodgerblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'darkviolet', 'purple', 'mediumvioletred']
colsel = collist1
angle = 85
interval = 2
turtle.bgcolor('black')
turtle.pensize(1)
turtle.tracer(10, 1)
colornum = 23


def loop():
    pensize = 1
    for i in range(1000):
        for j in range(colornum):
            ind = j % len(colsel)
            turtle.color(colsel[ind])
            turtle.forward((interval / colornum) * i)
        turtle.pensize(pensize)
        pensize = pensize * 1.1
        turtle.right(angle)




loop()