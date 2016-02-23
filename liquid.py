#!/usr/bin/env python

from gimpfu import *

def liquify (image, filename, percent, nrg_func):
    if filename and not image:
        image = pdb.gimp_file_load (filename, filename)
    if not image and not filename:
        raise "No image given."

    layers = image.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (image)
    if pdb.gimp_image_base_type (image) != 0:
        pdb.gimp_image_convert_rgb (image)
    width = pdb.gimp_image_width (image)
    height = pdb.gimp_image_height (image)
    i = 0
    while i < nlayers:
        w = int (width * (1.0 + (percent - 1) * (1 - i / float (nlayers))))
        h = int (height * (1.0 + (percent - 1) * (1 - i / float (nlayers))))
        pdb.plug_in_lqr (image, layers [i], w, h,
                         -1, -1, -1, -1, 0, -1, 1, 150, 1, 1, 0, 0,
                         nrg_func, 0, 0, 1, 1, 1, "", "", "", "")
        i += 1

    if filename:
        pdb.gimp_image_convert_indexed (image, 0, 0, 255, False, False, "palette")
        pdb.file_gif_save (image, drawable, filename, filename, 0, 1, 50, 0)

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
        (PF_STRING, "filename", "The filename of a copy to make", ""),
        (PF_FLOAT, "percent", "The percent to scale the animation to", 0.01),
        (PF_INT32, "nrg_func", "The energy function to use", 0),
    ],
    [],
    liquify, menu="<Image>/Filters/Animation")

main()
