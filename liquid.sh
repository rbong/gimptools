#!/usr/bin/env bash
filename=$1
percent=$2
nrg_func=$3
if [ "$2" == "" ]; then percent='0.01'; fi
if [ "$3" == "" ]; then nrg_func='0'; fi
gimp -i -b '(python-fu-batch-liquify RUN-NONINTERACTIVE '\"$filename\"' '$percent' '$nrg_func')' -b '(gimp-quit 0)'
