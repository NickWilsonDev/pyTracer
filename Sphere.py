# Sphere.py
""" Class models a sphere shape. """
import numpy as np

class Sphere(object):

    def __init__(self, center, radius, opacity, color):
        self.center  = center
        self.radius  = radius
        self.opacity = opacity
        self.color   = color
        self.radius_squared = self.radius * self.radius

    def solve_quadratic(self, a, b, c):
        answers = []
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            answers[0] = False
            return answers
        elif discriminant == 0:
            answers[0] = True
            answers[1] = -0.5 * b / a
            answers[2] = answers[0]
            return answers
        else:
            q = 0.0
            if b > 0:
                q = -0.5 * (b + math.sqrt(discriminant))
            elif b < 0:
                q = -0.5 * (b - math.sqrt(discriminant))
            answers[0] = True
            answers[1] = q / a;
            answers[2] = c / q;
    def hit(self, ray):
        """ We need origin of the ray, direction of the ray, and center of
            sphere.
        """
        #need to add more intersection
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

