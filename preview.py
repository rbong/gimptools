#!/usr/bin/env python2

from gimpfu import *
import time
import re

def preview (image, delay, loops, force_delay, ignore_hidden, restore_hide):
    if not image:
        raise "No image given."
    layers = image.layers
    nlayers = len (layers)
    visible = []
    length = []
    i = 0
    while i < nlayers:
        visible += [pdb.gimp_item_get_visible (layers [i])]
        if visible [i]:
            pdb.gimp_item_set_visible (layers [i], False)
        name = pdb.gimp_item_get_name (layers [i])
        l = None
        if not force_delay:
            l = re.search ("\([0-9]+ms\)", name)
            if l:
                l = tuple (map (sum, zip (l.span (), tuple ([+1, -3]))))
                l = name [slice (*l)]
        if not l:
            l = delay
        length += [float (l) / 1000.0]
        i += 1


    j = 0
    while j < loops:
        while i > 0:
            i -= 1
            if (not ignore_hidden) or visible [i]:
                pdb.gimp_item_set_visible (layers [i], True)
                pdb.gimp_displays_flush ()
                time.sleep (length [i])
        j += 1

        # unhides everything for optimized
        if j < loops:
            while i < nlayers:
                if (not ignore_hidden) or visible [i]:
                    pdb.gimp_item_set_visible (layers [i], False)
                i += 1

        else:
            i = nlayers

        i = nlayers


    if restore_hide:
        while i > 0:
            i -= 1
            if visible [i]:
                pdb.gimp_item_set_visible (layers [i], True)

register(
    "preview",
    "preview",
    "Preview the animation of a gif",
    "Roger Bongers",
    "Roger Bongers",
    "2016",
    "Preview...",
    "*",
    [
        (PF_IMAGE, "image", "The image to modify", None),
        (PF_INT32, "delay", "The default length in ms of each frame", 100),
        (PF_INT32, "loops", "The number of times to loop the animation", 1),
        (PF_BOOL, "force-delay", "Force the default length on every frame", 0),
        (PF_BOOL, "ignore-hidden", "Ignore currently hidden items", 0),
        (PF_BOOL, "restore-hide", "Restore the hidden status after preview", 0),
    ],
    [],
    preview,
    menu = "<Image>/Filters/Animation")

main()
