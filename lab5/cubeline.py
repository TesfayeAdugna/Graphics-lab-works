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
    glPointSize(1.6)
    glBegin(GL_POINTS)

    # first rectangle
    V1 = np.array([0,1])
    V2 = np.array([1,0])
    t1 = 4
    t2 = 6
    x0 = np.linspace(-6,6,10000)
    y0 = np.linspace(-4,4,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0_horizontal = [i,0]
        P0_vertical = [0,j]
        P1 = P0_horizontal + t1*V1
        glVertex2f(P1[0],P1[1])
        P2 = P0_horizontal + (-1 * t1*V1)
        glVertex2f(P2[0],P2[1])
        P3 = P0_vertical + t2*V2
        glVertex2f(P3[0],P3[1])
        P4 = P0_vertical + (-1 * t2*V2)
        glVertex2f(P4[0],P4[1])

    # second rectangle
    V1 = np.array([0,1])
    V2 = np.array([1,0])
    t1 = 4
    t2 = 6
    x0 = np.linspace(-4,8,10000)
    y0 = np.linspace(-2,6,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0_horizontal = [i,2]
        P0_vertical = [2,j]
        P1 = P0_horizontal + t1*V1
        glVertex2f(P1[0],P1[1])
        P2 = P0_horizontal + (-1 * t1*V1)
        glVertex2f(P2[0],P2[1])
        P3 = P0_vertical + t2*V2
        glVertex2f(P3[0],P3[1])
        P4 = P0_vertical + (-1 * t2*V2)
        glVertex2f(P4[0],P4[1])

    # the lines
    V = np.array([1,1])
    t = 0
    x0 = np.linspace(-6,-4,10000)
    y0 = np.linspace(4,6,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0 = [i,j]
        P = P0 + t*V
        glVertex2f(P[0],P[1])
        
    # line 2
    V = np.array([1,1])
    t = 0
    x0 = np.linspace(-6,-4,10000)
    y0 = np.linspace(-4,-2,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0 = [i,j]
        P = P0 + t*V
        glVertex2f(P[0],P[1])

    # line 3
    V = np.array([1,1])
    t = 0
    x0 = np.linspace(6,8,10000)
    y0 = np.linspace(-4,-2,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0 = [i,j]
        P = P0 + t*V
        glVertex2f(P[0],P[1])

    # line 4
    V = np.array([1,1])
    t = 0
    x0 = np.linspace(6,8,10000)
    y0 = np.linspace(4,6,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0 = [i,j]
        P = P0 + t*V
        glVertex2f(P[0],P[1])

    glEnd()
    glFlush()

def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()