# Ray.py
""" A ray is simply an origin point and a direction(3 dimensional vector)
"""
import numpy as np

class Ray(object):
    """ Primary rays start at camera origin and go through the image the
        specified image(x, y, 0) position, they then continue out into
        the scene.
    """
    def __init__(self, origin, direction):
        self.origin = np.asarray(origin)
        self.direction = np.asarray(direction)

