from gimpfu import *

def duplicate_all_layers (image, copies):
    filename=None
    if type (image) == type (str ()):
        filename=image
        image = pdb.gimp_file_load (filename, filename)

    layers = image.layers
    nlayers = len (layers)
    drawable = pdb.gimp_image_get_active_layer (image)
    i = nlayers
    while i > 0:
        i -= 1
        j = 0
        while j < copies:
            new_layer = pdb.gimp_layer_copy (layers [i], 1)
            pdb.gimp_image_insert_layer (image, new_layer, None, i)
            j += 1

    if filename:
        pdb.file_gif_save (image, drawable, filename, filename, 0, 1, 50, 0)

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
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT32, "copies", "The number of times to copy each layer", 1),
    ],
    [],
    duplicate_all_layers, menu="<Image>/Layer")

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
        (PF_STRING, "image", "The image to modify", None),
        (PF_INT32, "copies", "The number of times to copy each layer", 1),
    ],
    [],
    duplicate_all_layers)

main()
