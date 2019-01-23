#!/usr/bin/env bash
filename=$1
percent=${2:-0.01}
nrg_func=${3:-0}
cp "$filename" "$filename".bkp
gimp -i \
  -b '(python-fu-batch-liquify RUN-NONINTERACTIVE "'"$filename"'" '$percent' '$nrg_func')' \
  -b '(gimp-quit 0)'
