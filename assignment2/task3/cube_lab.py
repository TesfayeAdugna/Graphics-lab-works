import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import pyrr
import transform
from PIL import Image

vao, program, texture = None, None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "assignment2/task3/shaders", filename)
    return open(p, 'r').read()


def init():
    global vao, program, texture
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShader = compileShader(getFileContents(
        "triangle.vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents(
        "triangle.fragment.shader"), GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    vertexes = np.array([
        # position          # color           # texture s, r
        [0.5, 0.5,   0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [0.5, -0.5,  0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, 0.5,  0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [0.5, -0.5,  0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, -0.5, 0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [-0.5, 0.5,  0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        # the five new vertices
        # 1 back
        [0.5, 0.5, -0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [0.5, -0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [0.5, -0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, -0.5, -0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [-0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],
        # 2 left
        [0.5, 0.5, 0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [0.5, -0.5, 0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [0.5, -0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [0.5, -0.5, 0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],
        # 3 top
        [0.5, 0.5, 0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [-0.5, 0.5, 0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [-0.5, 0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [0.5, 0.5, -0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [-0.5, 0.5, 0.50,   0.0, 0.7, 0.2,    0.0, 1.0],
        # 4 right
        [-0.5, 0.5, 0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [-0.5, -0.5, 0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, 0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [-0.5, 0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, -0.5, -0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [-0.5, -0.5, 0.50,   0.0, 0.7, 0.2,    0.0, 1.0],
        # 5 bottom
        [-0.5, -0.5, 0.50,    1.0, 0.20, 0.8,   1.0, 1.0],
        [0.5, -0.5, 0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [-0.5, -0.5, -0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

        [-0.5, -0.5, -0.50,   1.0, 1.0, 0.0,    1.0, 0.0],
        [0.5, -0.5, -0.50,  0.0, 0.4, 1.0,    0.0, 0.0],
        [0.5, -0.5, 0.50,   0.0, 0.7, 0.2,    0.0, 1.0],

    ], dtype=np.float32)

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    glBindVertexArray(vao)

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    image = Image.open("assignment2/task3/images/kelly.jpg")
    width, height = image.size
    image_data = np.array(list(image.getdata()), dtype=np.uint8)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * vertexes.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * vertexes.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(1)

    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * vertexes.itemsize, ctypes.c_void_p(24))
    glEnableVertexAttribArray(2)


    # unbind VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # unbind VAO
    glBindVertexArray(0)

    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def draw(x):
    global vao, program, texture
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glUseProgram(program)
    glBindVertexArray(vao)
    glBindTexture(GL_TEXTURE_2D, texture)

    rotateMatLocation = glGetUniformLocation(program, "transform")

    rotateMat_x = transform.rotationMatrix_x(x%360)
    rotateMat_y = transform.rotationMatrix_y(x%360)
    rotateMat_z = transform.rotationMatrix_z(x%360)

    xy = pyrr.matrix44.multiply(rotateMat_x, rotateMat_y)

    glUniformMatrix4fv(rotateMatLocation, 1, GL_FALSE, pyrr.matrix44.multiply(xy, rotateMat_z))

    glDrawArrays(GL_TRIANGLES, 0, 36)
    
    glBindTexture(GL_TEXTURE_2D,0)
    glBindVertexArray(0)


def main():
    init()
    x = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw(x)
        x += 1
        pygame.display.flip()
        pygame.time.wait(10)


main()