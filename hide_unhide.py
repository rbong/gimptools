#!/usr/bin/env python2

from gimpfu import *

def hide_unhide (image, mode, start = 0, end = -1):
    layers = image.layers
    nlayers = len (layers)
    if end > nlayers or end < 0:
        end = nlayers
    if start <= 0:
        start = 1
    i = nlayers - end
    end = nlayers - start
    while i <= end:
        pdb.gimp_item_set_visible (layers [i], mode)
        i += 1
    pdb.gimp_displays_flush ()

def hide_all_layers (image):
    hide_unhide (image, 0)

def unhide_all_layers (image):
    hide_unhide (image, 1)

def hide_range (image, start, end):
    hide_unhide (image, 0, start, end)

def unhide_range (image, start, end):
    hide_unhide (image, 1, start, end)

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
    hide_all_layers,
    menu = "<Image>/Layer")

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
    unhide_all_layers, menu = "<Image>/Layer")

register(
    "hide_range",
    "hide_range",
    "Hide range",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Hide range",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT32, "start", "The beginning of the range", None),
        (PF_INT32, "end", "The end of the range", None),
    ],
    [],
    hide_range, menu = "<Image>/Layer")

register(
    "unhide_range",
    "unhide_range",
    "unHide range",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Unhide range",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT32, "start", "The beginning of the range", None),
        (PF_INT32, "end", "The end of the range", None),
    ],
    [],
    unhide_range, menu = "<Image>/Layer")

main ()
