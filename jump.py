#!/usr/bin/env python

from gimpfu import *

def jump (image, layer):
    if not image:
        raise "No image given."

    nlayers = len (image.layers)
    if layer < 0:
        layer = nlayers
    pdb.gimp_image_set_active_layer (image, image.layers [nlayers - layer - 1])

register(
    "jump-to-num",
    "jump-to-num",
    "Jumps to a layer by number",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Jump by number",
    "*",
    [
        (PF_IMAGE, "image", "The image with the layer to jump to", None),
        (PF_INT, "layer", "The layer number to jump to", 1),
    ],
    [],
    jump, menu="<Image>/Layer")
