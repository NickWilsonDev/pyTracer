# PyTracer.py
"""My attempt at writting a ray tracer in python. """


""" Should be called with command line arguments
    width  - dimension for final picture
    length - dimension for final picture
    sourcefile - file to read shapes positions ect.

    python PyTracer.py <width> <height> <sourcefile>
"""
import sys
import util as util

arguments = len(sys.argv) - 1
if arguments != 3:
    print "python PyTracer.py <width> <height> <sourcefile>"
    sys.exit()


""" set command line args to vars """
width = sys.argv[1]
height = sys.argv[2]
sourcefile = sys.argv[3]

# parse file and load up objects in obj_list and light_list
scene = util.load_file(sourcefile)
shape_list = scene[0]
light_list = scene[1]

print "Shape list :: " + str(shape_list)
print "Light list :: " + str(light_list)
#define some objects
#define lights
#define window whose surface is covered with pixels

"""
for each pixel
    shoot a ray towards the objects from the center of the pixel
    compute nearest hit point of the ray with the objects if any

    if the ray hits an object
    use objects material and the lights to compute the pixel color
    
    else
    set the pixel color to black
"""
