gimptools
=========

Plugins I have found useful to write for gimp.

usage
=====

Move the .py files to your ~/.gimp\*/plug-ins/ directory, then invoke them with

```
gimp -i -b '(command args)' -b '(gimp-quit 0)'
```

Or call them inside of gimp.

plug-ins
========

## rainbow.py

Cycles colors on a gif.

Rainbowfy is found inside of Filters/Animation.

![rainbow.scm](https://raw.githubusercontent.com/rbong/gimptools/master/examples/tree.gif)

## liquid.py

Uses liquid rescale incrementally on a gif.

Liquify is found inside of Filters/Animation.

## preview.py

Previews a gif inside gimp. Follows the delay of each frame or defaults to a
given delay, which can be forced. Optionally ignores hidden frames.

Preview is found inside of Filters/Animation.

## jump.py

Jumps to layer by number or name.

Jump by Name and Jump by Number are both found inside of the Layer/ menu

## dup\_all.py

Duplicate all the layers in an image a certain number of times.

Duplicate all Layers is found inside of the Layer/ menu.
