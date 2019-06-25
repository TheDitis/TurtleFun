import turtle


wn = turtle.Screen()
turtle.shape("circle")
turtle.penup()
# turtle.resizemode("auto")


def stamp_circle(s):
    # turtle.pensize(s)
    for i in range(10):
        turtle.forward(50)
        turtle.stamp()
        turtle.forward(-50)
        turtle.right(36)


wn.exitonclick()


for size in list(range(1, 10)):
    stamp_circle(size)