#!/bin/bash

./install-revealjs.sh
./fix-hash.sh

mkdir -p public
mkdir -p public/lectures
cp -rv presentations static media dist plugin css js public/lectures/
hugo build