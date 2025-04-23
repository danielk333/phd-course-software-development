#!/bin/bash

for filename in code/graphviz/*.gv; do
    filen=$(basename $filename)
    filen="${filen%%.*}.png"
    echo $filename
    dot -Tpng -oassets/$filen $filename
done
