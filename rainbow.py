#!/usr/bin/env python

from gimpfu import *
from gimptools import *

def alien (img, layer, red, green, blue, freq):
    pdb.plug_in_alienmap2 (img, layer,
            freq, red % 360, freq, green % 360, freq, blue % 360, 0, True, True, True)

def rainbowfy (image, loops, freq):
    f = lambda i, l, r, g, b: alien (i, l, r, g, b, freq)
    ramp (image, f, (0, 360, int), (180, 540, int), (360, 0, int))

register(
    "rainbowfy",
    "Rainbowfy",
    "Cycle colors of a gif",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "_Rainbowfy...",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT, "loops", "Number of times to cycle the color palette", 1),
        (PF_FLOAT, "frequency", "The color frequency", 1.2),
    ],
    [],
    rainbowfy,
    menu = "<Image>/Filters/Animation")

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
