import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


vertices1 = ( (5,-5), (5,5), (-5, 5), (5, -5), (-5, 5), (-5, -5) )

edges1 = ( (0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3) )

def Cube():
    glBegin(GL_LINES)
    # The first triangle
    for edge in edges1:
        for vertex in edge:
            glVertex2fv(vertices1[vertex])


    glEnd()


def main():
    init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[1] / display[0]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()