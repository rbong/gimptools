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
