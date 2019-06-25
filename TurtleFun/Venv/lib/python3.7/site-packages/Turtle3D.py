###################################################################################
#                      ©Javiera Del Escoval Bücher                                #
#                                2018                                             #
#                           javiswebsites.ga                                      #
###################################################################################
from turtle import *
from math import *

def leeVertices(fname):
    file = open(fname, 'r')
    vertices = []
    faces = []
    for line in file:
        if(line[0]== 'v' and line[1] != 'n'):
            s = line.split(" ")
            vertices.append([float(s[1]), float(s[2]), float(s[3])])
        if(line[0]== 'f'):
            s = line.split(" ")
            h = []
            for i in range(len(s)-1):
                h.append(s[i+1].split("//"))
                faces.append([int(h[i][0])-1, int(h[i][1])-1])
                if(i != 0 and i % 3 == 0):
                    faces.append([int(h[i-3][0])-1, int(h[i-3][1])-1])
    return vertices, faces

def setupWindow(w, h):
    setup(w, h)
    bgcolor('#adccff')

def rotationMatrix(axis, angle):
    matrix = [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]]
    if(axis == 'x'):
      matrix = [ [1, 0, 0],
                 [0, cos(radians(angle)), -sin(radians(angle))],
                 [0, sin(radians(angle)), cos(radians(angle))]]
    elif(axis == 'y'):
      matrix = [ [cos(radians(angle)), 0, sin(radians(angle))],
                 [0, 1, 0],
                 [-sin(radians(angle)), 0, cos(radians(angle))]]
    elif(axis == 'z'):
      matrix = [ [cos(radians(angle)), -sin(radians(angle)), 0],
                 [sin(radians(angle)), cos(radians(angle)), 0],
                 [0, 0, 1]]
    return matrix

def multiMatrices(matrix1, matrix2):
    matrix3 = [[0], [0], [0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[i])):
            for k in range(len(matrix2)):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
    return matrix3[0][0], matrix3[1][0], matrix3[2][0]

def drawModel(posx, posy, vertices, faces, colour, angle=0, sizeDiv=1):
    color(colour)
    pu()
    goto(posx,posy)
    width(2//sizeDiv)
    speed(0)
    for i in range(len(faces)):
        for j in range(len(vertices)):
            if(j == faces[i][0]):
                if(i > 1):
                    if(faces[i-1][1] != faces[i][1]):
                        pu()
                    else:
                        pd()
                x = vertices[j][0]
                y = vertices[j][1]
                z = vertices[j][2]
                cMatrix = [[x], [y], [z]]
                yrMatrix = rotationMatrix('y', angle)
                x, y, z = multiMatrices(yrMatrix, cMatrix)
                x = x*100//sizeDiv + posx
                y = y*100//sizeDiv + posy
                z = z*50//sizeDiv
                goto(x, y)
                pd()
