# Plane.py
""" Class models a infinite plane shape. """
import numpy as np

class Plane(object):

    def __init__(self, point, normal, color):
        self.point   = np.asarray(point)
        self.normal  = np.asarray(normal)
        self.color   = np.asarray(color)
        self.normal  = np.linalg.norm(self.normal)

    def hit(self, ray):
        denominator = np.dot(self.normal, ray.direction)
        if denominator > 0.0000001:
           pass
        answer = []
        return None

    def to_string(self):
        return "point: %s   normal:: %s" %(self.point, self.normal)

