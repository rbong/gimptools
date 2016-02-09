filename=$1
percent=$2
nrg_func=$3
if [ "$2" == "" ]; then percent='0.1'; fi
if [ "$3" == "" ]; then nrg_func=0; fi
gimp -i -b '(python-fu-liquify RUN-NONINTERACTIVE 0 '\"$filename\"' '$percent' '$nrg_func')' -b '(gimp-quit 0)'
