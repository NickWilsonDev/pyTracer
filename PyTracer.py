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
from PIL import Image
from Ray import Ray

#Black rgb
BACKGROUND_COLOR = np.asarray([0, 0, 0])
CAMERA_POSITION = np.asarray([0, 0, -10])

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

#pixels = np.zeros([image_width, image_height, 3], dtype = np.uint8)
pixels = Image.new("RGB", (image_width, image_height))
#pixels = []

#for i in range(0, image_width):
#    temprow = []
#    for j in range(0, image_height):
#        temprow.append([0, 0, 0])
#    pixels.append(temprow)

def map_pixel_to_world(x, y):
    # map pixel to world coordinates
    map_to_world = np.asarray([0.0, 0.0, 0.0])
    map_to_world[0] = float(x / (image_width - 1) * image_width)
    map_to_world[0] -= float(map_to_world[0] / 2.0)

    map_to_world[1] = float(x / (image_height - 1) * image_height)
    map_to_world[1] -= float(map_to_world[1] / 2.0)

    map_to_world[2] = 0.0
    return np.asarray(map_to_world)

    #def trace(ray

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
    for y in range(image_height):
        for x in range(image_width):
            #ray = Ray(CAMERA_POSITION, np.subtract(map_pixel_to_world(i, j), CAMERA_POSITION))
            ray = Ray(CAMERA_POSITION, np.subtract(map_pixel_to_world(x, y), CAMERA_POSITION)) # still need to normalize vector
            for shape in shape_list:
                # build primary ray
                # does it intersect with any objects
                distance = shape.hit(ray)
                if distance != None: # and object is closest
                    #set pixel point to color of sphere
                    #pixels[i][j] = shape.color
                    pixels.putpixel((y, x), (int(shape.color[0]), int(shape.color[1]), int(shape.color[2])))
                    print "hit---------------"
                    print shape.to_string()
                    print "x:: %d, y:: %d " % (x, y)
                    print shape.color
                    print "distance :: %f" % distance
                else:
                    #print j * image_width + i
                    #pixels[j * image_width + i - 1] = BACKGROUND_COLOR
                    pixels.putpixel((y, (image_width - 1) - x), (0, 0, 0))#(BACKGROUND_COLOR))
                    #pixels[i][j] = BACKGROUND_COLOR
    util.write_image(pixels)

render()

