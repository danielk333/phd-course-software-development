#!/bin/bash

./install-revealjs.sh
./fix-hash.sh

mkdir -p public
cp -rv presentations static media dist plugin css js public/