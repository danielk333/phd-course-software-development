#!/bin/bash

for filename in diagrams/*.gv; do
    filen=$(basename $filename)
    filen="${filen%%.*}.png"
    echo $filename
    dot -Tpng -ostatic/diagrams/$filen $filename
done
