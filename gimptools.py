#!/usr/bin/env python

from gimpfu import *

def ramp_sample (arg, n, length):
    start, end, cast = arg
    if None in (cast, end, n, length):
        return start
    return cast (start + (end - start) * n / float (length - 1))

def ramp_apply_at (func, img, layer, i, nlayers, arg):
    newarg = tuple (ramp_sample (a, i, nlayers) for a in arg)
    func (*((img, layer) + newarg))

def get_image (img):
    filename = None
    if type (img) == type (str ()):
        filename = img
        img = pdb.gimp_file_load (filename, filename)
    return img, filename

def ramp (img, func, *arg):
    img, filename = get_image (img)

    layers = img.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (img)
    if pdb.gimp_image_base_type (img) != 0:
        pdb.gimp_image_convert_rgb (img)

    i = 0
    while i < nlayers:
        ramp_apply_at (func, img, layers [i], i, nlayers, arg)
        i += 1

    if filename:
        pdb.gimp_image_convert_indexed (
            img, 0, 0, 255, FALSE, FALSE, "palette")
        pdb.file_gif_save (img, drawable, filename, filename, 0, 1, 50, 0)

