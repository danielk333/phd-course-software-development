#!/bin/bash
hugo build

mkdir -p public/lectures

./install-revealjs.sh
./fix-hash.sh
cp -rv static media dist plugin css js public/lectures/
for lect in presentations/*.html; do
    bname="$(basename $lect)"
    dname="${bname%.*}"
    cp "$lect" "public/lectures/$dname/index.html" -v
done