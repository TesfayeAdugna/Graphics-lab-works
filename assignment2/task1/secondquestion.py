import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
# declaring global variables.
triangleVAO, triangleEBO, program, indexes = None, None, None, None
# The function to load the file.
def getFileContents(filename):
    p = os.path.join(os.getcwd(), "assignment2/task1/shaders", filename)
    return open(p, 'r').read()
# Our init function
def init():
    global triangleVAO, triangleEBO, program, indexes
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(50, 50, 500, 500)
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
    vertexes = np.array([-0.75, -0.75, 0.0, 0.0, 0.0, 0.0,
                          0.75, -0.75, 0.0, 1.0, 0.5, 0.5,
                         -0.75,  0.75, 0.0, 0.5, 0.5, 0.7,
                          0.75,  0.75, 0.0, 0.0, 0.5, 0.5], dtype = np.float32)

    indexes = np.array([0, 1, 2,
                        1, 2, 3], dtype = np.uint32)

    # creating a space on GPU
    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)
    # loading the vertexes to the GPU.
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    # handling the arrays
    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)

    # creating the element object buffer
    triangleEBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, triangleEBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indexes.nbytes, indexes, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    
    # unbind VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # unbind VAO
    glBindVertexArray(0)

# draw function
def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)
    glBindVertexArray(triangleVAO)
    # glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)       # This line will be replaced by the following
    glDrawElements(GL_TRIANGLES, len(indexes), GL_UNSIGNED_INT, None)
    glBindVertexArray(0)
    
# The main function
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
        
# calling the main function
main()