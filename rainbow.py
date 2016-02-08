#!/usr/bin/env python

from gimpfu import *

def rainbowfy (image, filename, loops, frequency):
    if filename and not image:
        image = pdb.gimp_file_load (filename, filename)
    layers = image.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (image)
    pdb.gimp_image_convert_rgb (image)
    i = 0
    while i < nlayers:
        pdb.gimp_image_set_active_layer (image, layers [i])
        active_layer = pdb.gimp_image_get_active_layer (image)
        r_angle = (i * 360 * loops)/nlayers
        g_angle = r_angle + 180
        b_angle = 360 - r_angle
        pdb.plug_in_alienmap2 (image, active_layer,
                               frequency, r_angle,
                               frequency, g_angle,
                               frequency, b_angle,
                               0, True, True, True)
        i += 1

    if filename:
        pdb.gimp_image_convert_indexed (image, 0, 0, 255, False, False, "palette")
        pdb.file_gif_save (image, drawable, filename, filename, 0, 1, 50, 0)
        pdb.gimp_image_delete (image)

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
        (PF_STRING, "filename", "The filename of a copy to make.", ""),
        (PF_INT, "loops", "Number of times to cycle the color palette", 1),
        (PF_FLOAT, "frequency", "The color frequency", 1.2),
    ],
    [],
    rainbowfy, menu="<Image>/Filters/Animation")

main()
