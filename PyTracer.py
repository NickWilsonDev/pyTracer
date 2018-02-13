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
import numpy as np
from Ray import Ray

#Black rgb
BACKGROUND_COLOR = np.asarray([255, 255, 255])
CAMERA_POSITION = np.asarray([0, 0, -1])

arguments = len(sys.argv) - 1
if arguments != 3:
    print "python PyTracer.py <width> <height> <sourcefile>"
    sys.exit()


""" set command line args to vars """
image_width = int(sys.argv[1])
image_height = int(sys.argv[2])
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
# basically an array of (r, g, b) values, may need map to world function
rgb = np.asarray([0, 0, 0])
pixels = np.empty([image_width, image_height, 3], dtype = int)
"""
for each pixel
    shoot a ray towards the objects from the center of the pixel
    compute nearest hit point of the ray with the objects if any

    if the ray hits an object
    use objects material and the lights to compute the pixel color
    
    else
    set the pixel color to black
"""
def render():
    # distance from ray origin to hitpoint
    distance = 0.0
    for j in range(0, image_height):
        for i in range(0, image_width):
            for shape in shape_list:
                # build primary ray
                # does it intersect with any objects
                ray = Ray(CAMERA_POSITION, np.subtract(np.asarray([i, j, 0]), CAMERA_POSITION))
                if shape.hit(ray, distance):
                    #set pixel point to color of sphere
                    #print j * image_width + i
                    #pixels[j * image_width + i - 1] = shape.color
                    pixels[i][j] = shape.color
                    print "hit---------------"
                else:
                    #print j * image_width + i
                    #pixels[j * image_width + i - 1] = BACKGROUND_COLOR
                    pixels[i][j] = BACKGROUND_COLOR
    util.write_image(pixels)

render()
