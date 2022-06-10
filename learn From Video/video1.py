import glfw
from OpenGL.GL import *
import numpy as np
from math import cos, sin

class Window:
    def __init__(self, width:int, height:int, title:str):
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
                    0.0, 0.5, 0.0]
        colors = [1.0, 0.0, 0.0,
                  0.0, 1.0, 0.0,
                  0.0, 0.0, 1.0]
        vertices = np.array(vertices, dtype=np.float32)
        colors = np.array(colors, dtype=np.float32)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, colors)

        glClearColor(0, 0.1, 0.1, 1)


    def main_loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)

            ct = glfw.get_time()
            glLoadIdentity()
            glScale(abs(sin(ct)), abs(sin(ct)), 1)
            glRotatef(sin(ct)*45, 0, 0, 1)
            glTranslatef(sin(ct), cos(ct), 0)
            # glRotatef(0.2,0,1,0)

            glDrawArrays(GL_TRIANGLES, 0, 3)

            glfw.swap_buffers(self.window)

        glfw.terminate()


if __name__ == "__main__":
    win = Window(800, 600, "windows title")
    win.main_loop()