#!/bin/bash

# Magic sed to get hashes to work on pages with different subpaths
# TODO: get someone competent in JS to make this generalized
sed -i 's/presentations\//danielk-presentations\/presentations\//g' presentations/**/*.html