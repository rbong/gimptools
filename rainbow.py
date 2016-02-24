#!/usr/bin/env python

from gimpfu import *

def rainbowfy (image, loops, frequency):
    filename=None
    if type (image) == type (str ()):
        filename=image
        image = pdb.gimp_file_load (filename, filename)

    layers = image.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (image)
    if pdb.gimp_image_base_type (image) != 0:
        pdb.gimp_image_convert_rgb (image)
    i = 0
    while i < nlayers:
        r_angle = (i * 360 * loops)/nlayers
        g_angle = r_angle + 180
        b_angle = 360 - r_angle
        pdb.plug_in_alienmap2 (image, layers [i],
                               frequency, r_angle,
                               frequency, g_angle,
                               frequency, b_angle,
                               0, True, True, True)
        i += 1

    if filename:
        pdb.file_gif_save (image, drawable, filename, filename, 0, 1, 50, 0)

register(
    "rainbowfy",
    "Rainbowfy",
    "Cycle colors of a gif",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Rainbowfy...",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT, "loops", "Number of times to cycle the color palette", 1),
        (PF_FLOAT, "frequency", "The color frequency", 1.2),
    ],
    [],
    rainbowfy, menu="<Image>/Filters/Animation")

register(
    "batch-rainbowfy",
    "",
    "",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "",
    "*",
    [
        (PF_STRING, "image", "The image to modify", None),
        (PF_INT, "loops", "Number of times to cycle the color palette", 1),
        (PF_FLOAT, "frequency", "The color frequency", 1.2),
    ],
    [],
    rainbowfy)

main()
