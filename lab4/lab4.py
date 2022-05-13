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

    #first way for line
    V = np.array([0.3,0.4])
    t = 1
    x0 = np.linspace(1,8,10000)
    y0 = np.linspace(2,8,10000)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x0,y0):
        P0 = [i,j]
        P = P0 + t*V
        glVertex2f(P[0],P[1])


    # first way for rectangle
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

    # # Third way for rectangle
    # P0 = np.array([-6,4])
    # P01 = np.array([-6,-4])
    # P02 = np.array([6,-4])
    # t = 1
    # x = np.linspace(0,12,10000)
    # y = np.linspace(0,8,10000)
    # glColor3f(1.0, 0.0, 0.0)
    # for i,j in zip(x,y):
    #     V = [i,0]
    #     P = P0 + t*V # formula for the first horizontal line
    #     P1 = P01 + t*V # formula for the  second horizontal line
    #     glVertex2f(P[0],P[1])
    #     glVertex2f(P1[0],P1[1])
    #     V2 = [0,j]
    #     P = P01 + t*V2 # formula for the first vertical line
    #     P1 = P02 + t*V2 # formula for the second vertical line
    #     glVertex2f(P[0],P[1])
    #     glVertex2f(P1[0],P1[1])


    # second way for rectangle 
    # V1 = np.array([0,1])
    # V2 = np.array([1,0])
    # V3 = np.array([0,-1])
    # V4 = np.array([-1,0])
    # t1 = 4
    # t2 = 6
    # x0 = np.linspace(-6,6,1000)
    # y0 = np.linspace(-4,4,1000)
    # glColor3f(1.0, 0.0, 0.0)
    # for i,j in zip(x0,y0):
    #     P1 = [i,0] + t1*V1
    #     P2 = [i,0] + t1*V3
    #     P3 = [0,j] + t2*V2
    #     P4 = [0,j] + t2*V4
    #     glVertex2f(P1[0],P1[1])
    #     glVertex2f(P2[0],P2[1])
    #     glVertex2f(P3[0],P3[1])
    #     glVertex2f(P4[0],P4[1])

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