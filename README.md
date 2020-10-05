# gimptools

Plugins I have found useful to write for gimp.

![rainbow.scm](https://raw.githubusercontent.com/rbong/gimptools/master/examples/tree.gif)

## Dependencies

  - Gimp 2.10
  - Gimp Python bindings

## Installation

```bash
cp *.py ~/.config/GIMP/2.10/plug-ins/
rm ~/.config/GIMP/2.10/pluginrc
```

## Plug-ins

### rainbow.py

Cycles colors on a gif.

Rainbowfy is found inside of Filters/Animation.

There is also a batch-rainbowfy plugin intended for the command line. It can be
applied to a gif with ./rainbow.sh in the following fashion-

```bash
./rainbow.sh $filename ($loops) ($frequency)
```

Loops default is 1, frequency default is 1.2


### liquid.py

Uses liquid rescale incrementally on a gif.

Liquify is found inside of Filters/Animation.

There is also a batch-liquify plugin intended for the command line. It can be
applied to a gif with ./liquid.sh in the following fashion-

```bash
./liquid.sh $filename ($percent) ($nrg_func)
```

Percent default is 0.01, nrg\_func default is 0.

### preview.py

Previews a gif inside gimp. Follows the delay of each frame or defaults to a
given delay, which can be forced. Optionally ignores hidden frames.

Preview is found inside of Filters/Animation.

### jump.py

Jumps to layer by number or name.

Jump by Name and Jump by Number are both found inside of the Layer/ menu

### dup\_all.py

Duplicate all the layers in an image a certain number of times.

Duplicate all Layers is found inside of the Layer/ menu.

## Utilities

To use the utility functions provided by gimptools, simply include the
following line at the top of any python plugin in the local plugin directory.

```bash
from gimptools import *
```

### ramp

The ramp utility allows you to make a gimp animation plugin from any existing
gimp function.

The syntax is as follows:

```bash
ramp (image name, function, ...)
# variable argument list syntax
(start value, end value, typecast)
```

For examples, view liquid.py and rainbow.py
