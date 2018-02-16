# util.py
""" should contain helpful functions such as reading data from a file ect.
"""
from os import path
import sys
import numpy as np
""" should be pillow version 1.1.7 """
from PIL import Image
#from matplotlib.pyplot as plt

from Sphere import Sphere
from PointLight import PointLight
from Plane import Plane

shape_list = []
light_list = []

def norm(vector):
    total = 0
    for component in vector:
        total += component ** 2
    return math.sqrt(total)

def normalize(vector):
    new_vector = []
    for component in vector:
        new_vector.append(component / norm(vector))
    return new_vector

def load_file(filename):
    """ Reads source file specified in the parameter, and creates what 
        shapes that are specified. Then returns a list of shapes.
    """
    global shape_list
    global light_list
    line_group = []
    if path.isfile(filename) == False:
        sys.exit()
    else:
        input_file = open(filename, 'r')
        while True:
            line = input_file.readline()
            print line
            if "sphere" in line:
                print "sphere found"
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                load_sphere(line_group)
            elif "plane" in line:
                print "plane found"
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                load_plane(line_group)
            elif "plight" in line:
                print "plight found"
                line_group.append(input_file.readline().splitlines()[0])
                line_group.append(input_file.readline().splitlines()[0])
                load_plight(line_group)
            
            if not line:
                break
        scene = [shape_list, light_list]
        return scene

def load_plight(line_group):
    """ Reads data from source and creates a point light object """
    global light_list
    location = [float(x) for x in line_group[0].split()]
    color    = [float(x) for x in line_group[1].split()]
    plight = PointLight(location, color)
    light_list.append(plight)
    print "PointLight created"

def load_plane(line_group):
    """ Reads data from source and creates a infinite plane object """
    global shape_list
    position = [float(x) for x in line_group[0].split()]
    direction = [float(x) for x in line_group[1].split()]
    color = [float(x) for x in line_group[2].split()]
    plane = Plane(position, direction, color)
    shape_list.append(plane)
    print "Plane created"

def load_sphere(line_group):
    """ Reads data from source and creates a Sphere object """
    global shape_list
    position = [float(x) for x in line_group[0].split()]
    radius = [float(x) for x in line_group[1].split()]
    radius = radius[0]
    opacity = [float(x) for x in line_group[2].split()]
    color = [float(x) for x in line_group[3].split()]
    sphere = Sphere(position, radius, opacity, color)
    shape_list.append(sphere)
    print "sphere created"

def write_image(pixels):
    """Uses an NumPy array of pixels to write out an image to disk.
        Param pixels - an npArray of pixel values (R, G, B)
    """
    #pixels = pixels.flatten()
    #image = Image.fromarray(np.uint8(pixels))
    pixels.save('image.png') #may change file type later
