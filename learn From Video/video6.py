import glfw
from OpenGL.GL import *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr

class Window:
    def __init__(self, width:int, height:int, title:str):

        self.vertex_src = """
        # version 330

        layout(location = 0) in vec3 a_position;
        layout(location = 1) in vec3 a_color;

        uniform mat4 rotation;

        out vec3 v_color;

        void main()
        {
            gl_Position = rotation * vec4(a_position, 1.0);
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

        glfw.set_window_size_callback(self.window, self.Resize_Window)

        glfw.make_context_current(self.window)

        vertices = [-0.5, -0.5, 0.0,     1.0,  0.0, 0.0,
                    0.5, -0.5, 0.0,      0.0,  1.0, 0.0,
                    0.5,  0.5, 0.0,      0.5,  0.0, 1.0,
                   -0.5,  0.5, 0.0,      1.0,  1.0, 1.0,

                    -0.5, -0.5, -0.5,     1.0,  0.0, 0.0,
                     0.5, -0.5, -0.5,      0.0,  1.0, 0.0,
                     0.5,  0.5, -0.5,      0.5,  0.0, 1.0,
                    -0.5,  0.5, -0.5,      1.0,  1.0, 1.0,]

        self.indices = [0, 1, 2, 2, 3, 0,
                        4, 5, 6, 6, 7, 4,
                        4, 5, 1, 1, 0, 4,
                        6, 7, 3, 3, 2, 6,
                        5, 6, 2, 2, 1, 5,
                        7, 4, 0, 0, 3, 7]

        vertices = np.array(vertices, dtype=np.float32)
        self.indices = np.array(self.indices, dtype=np.uint32)

        shader = compileProgram(compileShader(self.vertex_src, GL_VERTEX_SHADER), compileShader(self.fragment_src, GL_FRAGMENT_SHADER))


        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))


        glUseProgram(shader)

        glClearColor(0, 0.1, 0.1, 1)

        glEnable(GL_DEPTH_TEST)

        self.rotation_loc = glGetUniformLocation(shader, "rotation")

    def Resize_Window(self, window, width, height):
        glViewport(0, 0, width, height)


    def main_loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            

            rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
            rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())

            # glUniformMatrix4fv(self.rotation_loc, 1, GL_FALSE, rot_x * rot_y)
            glUniformMatrix4fv(self.rotation_loc, 1, GL_FALSE, pyrr.matrix44.multiply(rot_x, rot_y) )

            # glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
            glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

            glfw.swap_buffers(self.window)

        glfw.terminate()


if __name__ == "__main__":
    win = Window(800, 600, "windows title")
    win.main_loop()