#!/usr/bin/env python

from gimpfu import *

def hide_all_layers (image):
    layers = image.layers
    nlayers = len (layers)
    i = 0
    while i < nlayers:
        pdb.gimp_item_set_visible (layers [i], 0)
        i += 1
    pdb.gimp_displays_flush ()

def unhide_all_layers (image):
    layers = image.layers
    nlayers = len (layers)
    i = 0
    while i < nlayers:
        pdb.gimp_item_set_visible (layers [i], 1)
        i += 1
    pdb.gimp_displays_flush ()

register(
    "hide_all_layers",
    "hide_all_layers",
    "Hide all layers",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Hide all Layers",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
    ],
    [],
    hide_all_layers, menu="<Image>/Layer")

register(
    "unhide_all_layers",
    "unhide_all_layers",
    "Unhide all layers",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Unhide all Layers",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
    ],
    [],
    unhide_all_layers, menu="<Image>/Layer")

main ()
