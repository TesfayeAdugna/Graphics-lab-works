from turtle import position
import glfw
from OpenGL.GL import *
import numpy as np
from math import cos, sin
from OpenGL.GL.shaders import compileProgram, compileShader

class Window:
    def __init__(self, width:int, height:int, title:str):

        self.vertex_src = """
        # version 330

        in vec3 a_position;
        in vec3 a_color;

        out vec3 v_color;

        void main()
        {
            gl_Position = vec4(a_position, 1.0);
            v_color = a_color;
        }
        """
        self.fragment_src = """
        # version 330

        in vec3 v_color;
        out vec4 out_color;

        void main()
        {
            out_color = vec4(v_color, 1.0);
        }
        """

        if not glfw.init():
            raise Exception("glfw can not be initialized")

        self.window = glfw.create_window(width, height, title, None, None)

        if not self.window:
            glfw.terminate()
            raise Exception("glfw window can not be created")

        glfw.set_window_pos(self.window, 200, 100)

        glfw.make_context_current(self.window)

        vertices = [-0.5, -0.5, 0.0,
                    0.5, -0.5, 0.0,
                    0.0,  0.5, 0.0,
                    1.0,  0.0, 0.0,
                    0.0,  1.0, 0.0,
                    0.0,  0.0, 1.0 ]

        vertices = np.array(vertices, dtype=np.float32)

        shader = compileProgram(compileShader(self.vertex_src, GL_VERTEX_SHADER), compileShader(self.fragment_src, GL_FRAGMENT_SHADER))


        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        position = glGetAttribLocation(shader, "a_position")
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        color = glGetAttribLocation(shader, "a_color")
        glEnableVertexAttribArray(color)
        glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(36))


        glUseProgram(shader)

        glClearColor(0, 0.1, 0.1, 1)


    def main_loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)

            glDrawArrays(GL_TRIANGLES, 0, 3)

            glfw.swap_buffers(self.window)

        glfw.terminate()


if __name__ == "__main__":
    win = Window(800, 600, "windows title")
    win.main_loop()