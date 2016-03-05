from gimpfu import *

def scale_at (arg, n, length):
    start, end, cast = arg
    if None in (cast, end, n, length):
        return start
    return cast (start + (end - start) * n / float (length - 1))

def wrap (func, img, layer, i, nlayers, arg):
    newarg = tuple (scale_at (a, i, nlayers) for a in arg)
    func (*((img, layer) + newarg))

def get_image (img):
    filename=None
    if type (img) == type (str ()):
        filename = img
        img = pdb.gimp_file_load (filename, filename)
    return img, filename


def scale (img, func, *arg):
    img, filename = get_image (img)

    layers = img.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (img)
    if pdb.gimp_image_base_type (img) != 0:
        pdb.gimp_image_convert_rgb (img)

    i = 0
    while i < nlayers:
        wrap (func, img, layers [i], i, nlayers, arg)
        i += 1

    if filename:
        pdb.gimp_image_convert_indexed (
            img, 0, 0, 255, FALSE, FALSE, "palette")
        pdb.file_gif_save (img, drawable, filename, filename, 0, 1, 50, 0)

