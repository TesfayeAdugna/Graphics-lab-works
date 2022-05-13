import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 1.0, 0.5, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    x = np.linspace(-10,10,10000)
    y = np.multiply(x,0)
    glPointSize(2)
    glBegin(GL_POINTS)
    for a, b in zip(x, y):
        glVertex2f(a,b)
        glVertex2f(b,a)

    glColor3f(1.0, 1.0, 0.0)
    x = np.linspace(-3,3,100)
    y = np.sqrt(9-(np.power(x,2)))
    for a,b in zip(x,y):
        glVertex2f(a,b)
        glVertex2f(a,-b)

    glColor3f(0.5, 0.0, 0.5)
    x = np.linspace(0.00001,10,10000)
    y = np.log(x)
    for a,b in zip(x,y):
        glVertex2f(a,b)
            
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
