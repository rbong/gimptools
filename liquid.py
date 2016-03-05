#!/usr/bin/env python

from gimpfu import *
from scale import *

def lqr (image, layer, w, h, nrg_func):
    pdb.plug_in_lqr (image, layer, w, h, -1, -1, -1, -1, 0, -1, 1, 150, 1, 1,
            0, 0, nrg_func, 0, 0, 1, 1, 1, "", "", "", "")

def liquify (img, percent, nrg_func):
    f = lambda i, l, w, h: lqr (i, l, w, h, nrg_func)
    _img = get_image (img) [0]
    w = pdb.gimp_image_width (_img)
    h = pdb.gimp_image_height (_img)
    _img = None
    scale (img, f, (w * percent, w, round), (h * percent, h, round))

register(
    "liquify",
    "Liquify",
    "Perform incremental liquid rescale on a gif",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Liquify...",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_FLOAT, "percent", "The percent to scale the animation to", 0.01),
        (PF_INT32, "nrg_func", "The energy function to use", 0),
    ],
    [],
    liquify, menu="<Image>/Filters/Animation")

register(
    "batch-liquify",
    "",
    "",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "",
    "*",
    [
        (PF_STRING, "image", "The image to modify", None),
        (PF_FLOAT, "percent", "The percent to scale the animation to", 0.01),
        (PF_INT32, "nrg_func", "The energy function to use", 0),
    ],
    [],
    liquify)

main()
