import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import transform

from regex import R
# declaring global variables.
triangleVAO, program = None, None
# The function to load the file.
def getFileContents(filename):
    p = os.path.join(os.getcwd(), "assignment2/task2/shaders", filename)
    return open(p, 'r').read()
# Our init function
def init():
    global triangleVAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(0, 0, 500, 500)
    # Reading the the vertex and fragment shader files.
    vertexShaderContent = getFileContents("triangle.vertex.shader")
    fragmentShaderContent = getFileContents("triangle.fragment.shader")
    # compiling the above shader files.
    vertexShader = compileShader(vertexShaderContent,GL_VERTEX_SHADER)
    fragmentShader = compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
    # creating a program that can run and attach the compiled shaders.
    program = glCreateProgram()
    glAttachShader(program,  vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)
    # creating triangle vertexes using numpy.
    vertexes = np.array([
        # vertex positions    # vertex colors
        [0.5, 0.0, 0.0,         1.0, 0.0, 0.0],
        [-0.5, 0.0, 0.0,        0.0, 1.0, 0.0],
        [0, 0.5, 0.0,           0.0, 0.0, 1.0]], dtype= np.float32)
    # creating a space on GPU
    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)
    # loading the vertexes to the GPU.
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    # handling the arrays
    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)
    positionLocation = glGetAttribLocation(program,"position")
    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE, 6*vertexes.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(positionLocation)

    colorLocation = glGetAttribLocation(program, "color");
    glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE, 6 * vertexes.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(colorLocation)
    # unbind VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # unbind VAO
    glBindVertexArray(0)

    # rotateMatLocation = glGetUniformLocation(program, "transform")
# draw function
def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)
    glBindVertexArray(triangleVAO)

    rotateMatLocation = glGetUniformLocation(program, "transform")
    rotateMat = transform.rotationMatrix_z(90)
    glUniformMatrix4fv(rotateMatLocation, 1, GL_FALSE, rotateMat)

    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)

# The main function
def main():
    init()
    x = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
# calling the main function
main()