#!/usr/bin/env bash
filename=$1
loops=${2:-1}
frequency=${3:-1.2}
gimp -i \
  -b '(python-fu-batch-rainbowfy RUN-NONINTERACTIVE "'"$filename"'" '$loops' '$frequency')' \
  -b '(gimp-quit 0)'
