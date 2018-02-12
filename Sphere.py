# Sphere.py
""" Class models a sphere shape. """
import numpy as np

class Sphere(object):

    def __init__(self, center, radius, opacity, color):
        self.center  = center
        self.radius  = radius
        self.opacity = opacity
        self.color   = color

    def hit(self, ray):
        """ We need origin of the ray, direction of the ray, and center of
            sphere.
        """
        
        # move sphere to origin to make math easier
        center_sphere = np.array(self.center)
        center_sphere = np.subtract(center_sphere, center_sphere)

        # origin of ray - self.center = new base

        #np.dot(a, b)
        b = 2 * np.dot(new_ray_origin, direction_ray)

        c = np.dot(new_ray_origin, new_ray_origin) - (self.radius ** 2)

        pass

    def to_string(self):
        return "center: %s   radius:: %s" %(self.center, self.radius)

