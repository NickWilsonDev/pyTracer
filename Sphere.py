# Sphere.py
""" Class models a sphere shape. """
import numpy as np
import math

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

    def solve_quadratic(self, a, b, c):
        answers = []
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            answers.append(False)
            return answers
        elif discriminant == 0:
            answers.append(True)
            answers.append(-0.5 * b / a)
            answers.append(answers[1])
            return answers
        else:
            q = 0.0
            if b > 0:
                q = -0.5 * (b + math.sqrt(discriminant))
            elif b < 0:
                q = -0.5 * (b - math.sqrt(discriminant))
            answers.append(True)
            answers.append(q / a);
            answers.append(c / q);
        return answers

    def hit(self, ray, distance):
        """ We need origin of the ray, direction of the ray, and center of
            sphere.
        """
        #need to add more intersection
        # move sphere to origin to make math easier
        center_sphere = self.center
        L = np.subtract(ray.origin, self.center)
        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(ray.direction, L)

        c = np.dot(L, L) - (self.radius ** 2)
        answers = self.solve_quadratic(a, b, c)
        if not answers[0]:
            return False
        
        if answers[1] > answers[2]:
            #swap values
            temp = answers[2]
            answers[2] = answers[1]
            answers[1] = temp

        if answers[1] < 0:
            answers[1] = answers[2]
            if answers[1] < 0:
                return False
        
        distance = answers[1]
        return True


    def to_string(self):
        return "center: %s   radius:: %s" %(self.center, self.radius)

