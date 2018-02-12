# Plane.py
""" Class models a infinite plane shape. """

class Plane(object):

    def __init__(self, point, normal, color):
        self.point   = point
        self.normal  = normal
        self.color   = color

    def hit(self):
        pass

    def to_string(self):
        return "point: %s   normal:: %s" %(self.point, self.normal)

