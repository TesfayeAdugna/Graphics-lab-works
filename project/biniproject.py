import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np

def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_LINES)
    glVertex2f(0.0,5.0)
    glVertex2f(0.0,-5.0)
    glVertex2f(5.0,0.0)
    glVertex2f(-5.0,0.0)
    v=np.array([1,0])
    glColor3f(1.0, 0.0, 0.0)

    t=4
    p0=np.array([-2,2])
    p=p0 + t*v
    glVertex2f(p0[0],p0[1])
    glVertex2f(p[0],p[1])


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