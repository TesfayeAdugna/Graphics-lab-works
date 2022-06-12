import numpy as np

def rotationMatrix_x(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [1, 0,               0,              0],
        [0, np.cos(radian), -np.sin(radian), 0],
        [0, np.sin(radian),  np.cos(radian), 0],
        [0, 0,               0,              1]
    ])

    return mat

def rotationMatrix_y(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian),  0,  np.sin(radian),   0],
        [0,               1,  0,                0],
        [-np.sin(radian), 0,  np.cos(radian),   0],
        [0,               0,  0,                1]
    ])

    return mat

def rotationMatrix_z(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian), 0, 0],
        [np.sin(radian),  np.cos(radian), 0, 0],
        [0,               0,              1, 0],
        [0,               0,              0, 1]
    ])

    return mat