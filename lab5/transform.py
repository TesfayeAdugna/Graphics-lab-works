import pygame
from OpenGL.GL import *
import numpy as np
from OpenGL.GLU import *
from pygame.locals import *

def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.4)
    glBegin(GL_POINTS)
    
    #x-y coordinates
    x = np.linspace(-10,10,10000)
    y = 0 * x
    glColor3f(0.0, 0.5, 0.0)
    for i,j in zip(x,y):
        glVertex2f(i,j)
        glVertex2f(j,i)

    # first way for rectangle
    V1 = np.array([0,1])
    V2 = np.array([1,0])
    t1 = 4
    t2 = 6
    x0 = np.linspace(-6,6,10000)
    y0 = np.linspace(-4,4,10000)
    glColor3f(1.0, 0.0, 0.0)
    M = rotationMatrix(60)
    for i,j in zip(x0,y0):
        P0_horizontal = [i,0]
        P0_vertical = [0,j]
        P1 = P0_horizontal + t1*V1
        xr,yr = np.dot(P1,M)
        glVertex2f(xr,yr)
        P2 = P0_horizontal + (-1 * t1*V1)
        xr,yr = np.dot(P2,M)
        glVertex2f(xr,yr)
        P3 = P0_vertical + t2*V2
        xr,yr = np.dot(P3,M)
        glVertex2f(xr,yr)
        P4 = P0_vertical + (-1 * t2*V2)
        xr,yr = np.dot(P4,M)
        glVertex2f(xr,yr)

    glEnd()
    glFlush()

def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    return mat

vertices= ((1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, 1),(1, 1, 1),(-1, -1, 1),(-1, 1, 1))
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()