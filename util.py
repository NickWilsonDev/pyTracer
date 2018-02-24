# util.py
""" should contain helpful functions such as reading data from a file ect.
"""
from os import path
import sys
import numpy as np
""" should be pillow version 1.1.7 """
from PIL import Image
import math

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
    world_size = []
    scene = []
    if path.isfile(filename) == False:
        sys.exit()
    else:
        input_file = open(filename, 'r')
        while True:
            line = input_file.readline()
            # grab world size of screen
            line_group = []
            print line
            if "world" in line:
                print "Grabbing world coordinate size of screen..."
                world_size = line.split()
                del world_size[0]
                world_size[0] = int(world_size[0])
                world_size[1] = int(world_size[1])
                print "World size (%d, %d)" % (world_size[0], world_size[1])
            elif "sphere" in line:
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
        scene.append(world_size)
        scene.append(shape_list)
        scene.append(light_list)
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

def write_ppm(pixels):
    header = "P3 {} {} 255\n".format(len(pixels[0]), len(pixels))
    img_data_rows = []
    for row in pixels:
        pixel_strs = [
            " ".join([str(int(color)) for color in pixel]) for pixel in row]
        img_data_rows.append(" ".join(pixel_strs))
    pixels = header + "\n".join(img_data_rows)

    with open("image.ppm", "w") as img:
        img.write(pixels)

def write_image(pixels):
    """Uses an NumPy array of pixels to write out an image to disk.
        Param pixels - an npArray of pixel values (R, G, B)
    """
    #pixels = pixels.flatten()
    #image = Image.fromarray(np.uint8(pixels))
    pixels.save('image.png') #may change file type later
