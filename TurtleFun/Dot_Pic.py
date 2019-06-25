import turtle
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image_file = Image.open("Test_Color.png")
image_file3 = image_file.convert('1')
image_file3.save('Test_B&W.png')
imgData = np.asarray(image_file3)

img = mpimg.imread('Test_B&W.png')
imgplot = plt.imshow(img)


pixarray = np.array(img)
pixarray = pixarray.astype(np.int64)


# turtle.tracer(8, 1)
# turtle.penup()
# coordlist = []


def __main__():
    coordlist = []
    for i in range(10000):
        randcoord = [np.random.randint(-500, 500), np.random.randint(-500, 500)]
        print(randcoord)
        coordlist.append(randcoord)
    for xy in coordlist:
        pass
    #     turtle.goto(xy)
        # transx, transy = (randcoord[0] * 1.836) + 918, (randcoord[1] * 1.836) + 918
        # if pixarray[transy][transx] == 1:
        #     turtle.dot()


__main__()
