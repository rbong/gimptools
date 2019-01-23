#!/usr/bin/env python

from gimpfu import *

def duplicate_all_layers (img, copies):
    filename = None
    if type (img) == type (str ()):
        filename = img
        img = pdb.gimp_file_load (filename, filename)

    layers = img.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (img)
    i = nlayers
    while i > 0:
        i -= 1
        j = 0
        while j < copies:
            new_layer = pdb.gimp_layer_copy (layers [i], 1)
            pdb.gimp_image_insert_layer (img, new_layer, None, i)
            j += 1

    if filename:
        pdb.file_gif_save (img, drawable, filename, filename, 0, 1, 50, 0)

register(
    "duplicate_all_layers",
    "duplicate_all_layers",
    "Perform incremental liquid rescale on a gif",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Duplicate all Layers",
    "*",
    [
        (PF_IMAGE, "img", "The image to modify", None),
        (PF_INT32, "copies", "The number of times to copy each layer", 1),
    ],
    [],
    duplicate_all_layers,
    menu = "<Image>/Layer")

register(
    "batch-duplicate-all-layers",
    "",
    "",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "",
    "*",
    [
        (PF_STRING, "img", "The image to modify", None),
        (PF_INT32, "copies", "The number of times to copy each layer", 1),
    ],
    [],
    duplicate_all_layers)

main()
