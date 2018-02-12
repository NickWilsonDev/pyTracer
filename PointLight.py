# PointLight.py
""" Class models a point light. """

class PointLight(object):

    def __init__(self, location, color):
        self.location   = location
        self.color   = color

    def hit(self):
        """ This object does not stop any light just emits it
        """
        pass

    def to_string(self):
        return "location: %s   color:: %s" %(self.location, self.color)

