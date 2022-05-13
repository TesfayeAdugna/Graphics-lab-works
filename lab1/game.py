import pygame
import glfw

if not glfw.init():
    raise Exception("glfw can't be initiated")

window = glfw.create_window(800, 500, "My first window for game",None,None)

if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created")

glfw.set_window_pos(window,100,100)

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()