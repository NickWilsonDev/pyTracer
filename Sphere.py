# Sphere.py
""" Class models a sphere shape. """
import numpy as np
import math
import util

class Sphere(object):

    def __init__(self, center, radius, opacity, color):
        print "------------Sphere----------"
        print center
        print radius
        self.center  = np.asarray(center)
        self.radius  = radius
        self.opacity = opacity
        self.color   = np.asarray(color)
        self.radius_squared = float(self.radius * self.radius)

    def get_surface_normal(self, point):
        surface = np.subtract(np.asarray(point), self.center)
        #still need to normalize and return
        return util.normalize(surface)

    def hit(self, ray):
        """ We need origin of the ray, direction of the ray, and center of
            sphere.
            Should return the distance the ray has traveled to hit the sphere,
            and 'None' otherwise
        """
        #need to add more intersection
        # move sphere to origin to make math easier
        sphere_to_ray = np.subtract(ray.origin, self.center)
        b = 2 * np.dot(ray.direction, sphere_to_ray)
        c = np.dot(sphere_to_ray, sphere_to_ray) - self.radius_squared
        discr_t = (b ** 2) - (4 * c)
        
        #print "discriminant::" 
        #print discr_t
        if discr_t >= 0:
            dist = (-b - math.sqrt(discr_t)) / 2
            if dist > 0:
                return dist
        return -10

    def to_string(self):
        return "center: %s   radius:: %s" %(self.center, self.radius)

