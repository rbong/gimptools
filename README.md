gimptools
=========

In the future, this will have multiple scripts I have found useful to write for
gimp. For now, it features one; a tool that can cycle throught the alien colour
filter to create pulsating colour images.

usage
=====

Move the .py files to your ~/.gimp\*/plug-ins/ directory, then invoke them with

```
gimp -i -b '(command args)' -b '(gimp-quit 0)'
```

Or call them inside of gimp. An example is shown in rainbow.sh.

examples
========

## rainbowfy.py

Rainbowfy is found inside of Filters/Animation

![rainbow.scm](https://raw.githubusercontent.com/rbong/gimptools/master/examples/tree.gif)
