#!/usr/bin/env bash
filename=$1
loops=$2
frequency=$3
if [ "$2" == "" ]; then loops=1; fi
if [ "$3" == "" ]; then frequency='1.2'; fi
gimp -i -b '(python-fu-batch-rainbowfy RUN-NONINTERACTIVE '\"$filename\"' '$loops' '$frequency')' -b '(gimp-quit 0)'
